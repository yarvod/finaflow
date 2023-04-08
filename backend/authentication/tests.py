from http.cookies import SimpleCookie
from unittest import mock

from django.contrib.auth import get_user_model
from django.contrib.auth.tokens import default_token_generator
from rest_framework.test import APITestCase
from rest_framework.test import APIClient
from django.urls import reverse
from rest_framework import status
from authentication.services import redis_instance

User = get_user_model()


class JWTEmailPassLoginTests(APITestCase):
    fixtures = ["test_user.json"]

    def setUp(self) -> None:
        self.login_url = reverse("api:authentication:login")
        self.check_url = reverse("api:users:me")
        self.user = User.objects.all().first()
        self.redis = redis_instance
        self.client = APIClient()
        self.client.logout()

    def tearDown(self) -> None:
        self.redis.hdel(str(self.user.id), "hash")
        self.user.delete()

    def test_login_wrong_credentials(self):
        """Testing login with wrong username and password"""

        resp = self.client.post(
            self.login_url,
            {"email": "wrongemail@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        resp = self.client.post(
            self.login_url,
            {"email": "testuser@phystech-job.ru", "password": "wrongpwd"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)
        resp = self.client.post(
            self.login_url, {"email": None, "password": "pa1ss"}, format="json"
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_wrong_access_token(self):
        resp = self.client.post(
            self.login_url,
            {"email": "testuser@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.client.cookies = SimpleCookie({"access_token": "11111"})
        resp = self.client.post(self.check_url)
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_username_pass_login(self):
        """Testing login with correct username and password
        Check if access & refresh tokens are inside cookie
        Test acccess token against protected resource"""
        # SECURE_SSL_REDIRECT is a SecurityMiddleware setting. Don't unit test third-party code.
        # Making sure that your code always uses SSL is a good goal. However, this is an integration testing problem.
        # The right tool for this job is Selenium + LiveServerTestCase.
        resp = self.client.post(
            self.login_url,
            {"email": "testuser@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.assertTrue("access_token" and "refresh_token" in resp.cookies)
        resp = self.client.get(self.check_url)  # with cookie
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        self.client.cookies = SimpleCookie()
        resp = self.client.post(self.check_url)  # without cookie
        self.assertEqual(resp.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_user_inactive(self):
        self.user.is_active = False
        self.user.save()
        resp = self.client.post(
            self.login_url,
            {"email": "testuser@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertFalse("access_token" and "refresh_token" in resp.cookies)


class TokenRefreshTests(APITestCase):
    fixtures = ["test_user.json"]

    def setUp(self) -> None:
        login_url = reverse("api:authentication:login")
        self.client = APIClient()
        resp = self.client.post(
            login_url,
            {"email": "testuser@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.redis = redis_instance
        self.user = User.objects.all().first()
        self.access_token = resp.cookies["access_token"].value
        self.refresh_token = resp.cookies["refresh_token"].value
        self.refresh_url = reverse("api:authentication:refresh")

    def tearDown(self) -> None:
        self.redis.hdel(str(self.user.id), "hash")
        self.user.delete()

    def test_no_credentials(self):
        """Test token refresh endpoint with no access token header
        Client shouldn't be able to obtain refresh token without cookie"""
        client = APIClient()
        response = client.post(self.refresh_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_wrong_refresh_token(self):
        """Test token refresh endpoint against wrong refresh token"""
        self.client.cookies = SimpleCookie({"refresh_token": "11111"})
        response = self.client.post(self.refresh_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_access_token_and_valid_refresh_token(self):
        """Test token refresh endpoint against correct refresh token"""

        response = self.client.post(self.refresh_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertTrue("access_token" and "refresh_token" in response.cookies)
        self.assertNotEquals(
            self.refresh_token, response.cookies["refresh_token"].value
        )
        self.assertNotEquals(self.access_token, response.cookies["access_token"].value)
        check_url = reverse("api:users:me")
        response = self.client.get(check_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_no_hash_in_redis(self):
        """Test there is no hash of token in Redis"""

        self.redis.hdel(str(self.user.id), "hash")
        response = self.client.post(self.refresh_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class TokenDestroyTests(APITestCase):
    fixtures = ["test_user.json"]

    def setUp(self) -> None:
        login_url = reverse("api:authentication:login")
        self.client = APIClient()
        resp = self.client.post(
            login_url,
            {"email": "testuser@phystech-job.ru", "password": "pa1ss"},
            format="json",
        )
        self.redis = redis_instance
        self.user = User.objects.all().first()
        self.access_token = resp.cookies["access_token"].value
        self.refresh_token = resp.cookies["refresh_token"].value
        self.logout_url = reverse("api:authentication:logout")

    def tearDown(self) -> None:
        self.redis.hdel(str(self.user.id), "hash")
        self.user.delete()

    def test_token_unauthorized(self):
        """Test token destroy endpoint with unauthorized users"""
        self.client.cookies = SimpleCookie()
        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)

    def test_token_destroy(self):
        """Test token destroy endpoint"""

        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        hash_exists = self.redis.hget(str(self.user.id), "hash")
        self.assertIsNone(hash_exists)

    def test_try_login_destroyed_token(self):
        """Test accessing protected endpoint after token destroy endpoint"""

        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_205_RESET_CONTENT)
        hash_exists = self.redis.hget(str(self.user.id), "hash")
        self.assertIsNone(hash_exists)
        response = self.client.post(self.logout_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_401_UNAUTHORIZED)


class RegisterUser(APITestCase):
    def setUp(self) -> None:
        self.login_url = reverse("api:authentication:login")
        self.register_url = reverse("api:authentication:register")
        self.activation_url = reverse("api:authentication:activate")
        self.resend_url = reverse("api:authentication:activate-resend")
        self.check_url = reverse("api:users:me")
        self.redis = redis_instance
        self.client = APIClient()
        self.data = dict(
            email="testuser@phystech-job.ru",
            first_name="newuser",
            last_name="newuser",
            password="newuserpassword",
            password2="newuserpassword",
        )

    def tearDown(self) -> None:
        User.objects.all().delete()

    @mock.patch("authentication.tasks.send_activation_email")
    def test_register(self, send_activation_email_mock):
        resp = self.client.post(self.register_url, data=self.data)
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)
        send_activation_email_mock.apply_async.assert_called_once_with(
            kwargs=dict(to_email=self.data["email"])
        )
        user = User.objects.get(email=resp.data["email"])
        self.assertEqual(user.is_active, False)
        token = default_token_generator.make_token(user)
        resp = self.client.post(
            self.activation_url, data=dict(uid=user.id, token=token)
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        user.refresh_from_db()
        self.assertEqual(user.is_active, True)

    @mock.patch("authentication.tasks.send_activation_email")
    def test_resend_activation(self, send_activation_email_mock):
        resp = self.client.post(self.register_url, data=self.data, format="json")
        self.assertEqual(resp.status_code, status.HTTP_201_CREATED)

        resp = self.client.post(self.resend_url, data={"email": self.data["email"]})
        send_activation_email_mock.apply_async.assert_called_with(
            kwargs=dict(to_email=self.data["email"])
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    @mock.patch("authentication.tasks.send_activation_email")
    def test_fail_resend_activation(self, send_activation_email_mock):
        resp = self.client.post(
            self.resend_url, data={"email": "wrongemail@phystech-job.ru"}
        )
        send_activation_email_mock.assert_not_called()
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)


class ResetPasswordTests(APITestCase):
    fixtures = ["test_user.json"]

    def setUp(self) -> None:
        self.password_reset_confirm_url = reverse(
            "api:authentication:password-reset-confirm"
        )
        self.password_reset_url = reverse("api:authentication:password-reset")
        self.login_url = reverse("api:authentication:login")
        self.client = APIClient()
        self.user = User.objects.all().first()
        self.token = default_token_generator.make_token(self.user)

    def tearDown(self) -> None:
        User.objects.all().delete()

    def test_success_change_password(self):
        resp = self.client.post(
            self.password_reset_confirm_url, data={"email": self.user.email}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.post(
            self.password_reset_url,
            data={
                "uid": self.user.id,
                "token": self.token,
                "password": "newpasswordforuser",
                "password2": "newpasswordforuser",
            },
        )

        self.assertEqual(resp.status_code, status.HTTP_200_OK)

    def test_incorrect_email(self):
        resp = self.client.post(
            self.password_reset_confirm_url,
            data={"email": "wrongemail@phystech-job.ru"},
        )
        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incorrect_token(self):
        resp = self.client.post(
            self.password_reset_confirm_url, data={"email": self.user.email}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)
        resp = self.client.post(
            self.password_reset_url,
            data={
                "uid": self.user.id,
                "token": "incorrecttoken",
                "password": "newpasswordforuser",
                "password2": "newpasswordforuser",
            },
        )

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_incorrect_uid(self):
        resp = self.client.post(
            self.password_reset_confirm_url, data={"email": self.user.email}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(
            self.password_reset_url,
            data={
                "uid": 250,
                "token": self.token,
                "password": "newpasswordforuser",
                "password2": "newpasswordforuser",
            },
        )

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)

    def test_password_mismatch(self):
        resp = self.client.post(
            self.password_reset_confirm_url, data={"email": self.user.email}
        )
        self.assertEqual(resp.status_code, status.HTTP_200_OK)

        resp = self.client.post(
            self.password_reset_url,
            data={
                "uid": self.user.id,
                "token": self.token,
                "password": "newpasswordforuser2",
                "password2": "newpasswordforuser",
            },
        )

        self.assertEqual(resp.status_code, status.HTTP_400_BAD_REQUEST)
