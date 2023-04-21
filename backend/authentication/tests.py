from django.contrib.auth import get_user_model
from unittest import mock
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase, APIClient

from authentication.services import generate_refresh_token

User = get_user_model()


class TokenRefreshTests(APITestCase):
    fixtures = ["test_user.json"]

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.all().first()
        cls.refresh_token = generate_refresh_token(user=cls.user)
        cls.refresh_url = reverse("api:authentication:refresh")

    def test_no_credentials(self):
        """Test token refresh endpoint with no access token header
        Client shouldn't be able to obtain refresh token
        without cookie"""

        client = APIClient()
        response = client.post(self.refresh_url, format="json")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    @mock.patch("authentication.services.get_refresh_token")
    def test_wrong_refresh_token(self, get_token):
        """Test token refresh endpoint
        against wrong refresh token"""

        get_token.return_value = False
        response = self.client.post(
            self.refresh_url, data={"RefreshToken": "11111"}, format="json"
        )

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)
        self.assertEqual(response.data["detail"], "Token is invalid")

    @mock.patch("authentication.services.get_refresh_token")
    @mock.patch("authentication.services.remove_refresh_token")
    @mock.patch("authentication.services.set_refresh_token")
    def test_valid_refresh_token(self, set_token, remove_token, get_token):
        """Test token refresh endpoint
        against correct refresh token"""

        get_token.return_value = True
        remove_token.return_value = True
        set_token.return_value = True
        response = self.client.post(
            self.refresh_url, data={"RefreshToken": self.refresh_token}, format="json"
        )
        print(response.data)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIn("AccessToken", response.data)
        self.assertIn("RefreshToken", response.data)
        for f in (get_token, remove_token):
            f.assert_called_with(user_id=str(self.user.id), token=self.refresh_token)
        set_token.assert_called_with(
            user_id=str(self.user.id), token=response.data["RefreshToken"]
        )


class LogoutTests(APITestCase):
    fixtures = ["test_user.json"]

    @classmethod
    def setUpTestData(cls):
        cls.client = APIClient()
        cls.user = User.objects.all().first()
        cls.logout_url = reverse("api:authentication:logout")

    @mock.patch("authentication.services.remove_all_tokens")
    def test_correct_logout(self, remove_tokens):
        remove_tokens.return_value = True
        self.client.force_authenticate(user=self.user)
        resp = self.client.post(self.logout_url)
        self.assertEqual(resp.status_code, 205)

    @mock.patch("authentication.services.remove_all_tokens")
    def test_invalid_logout(self, remove_tokens):
        remove_tokens.return_value = False
        self.client.force_authenticate(user=self.user)
        resp = self.client.post(self.logout_url)
        self.assertEqual(resp.status_code, 400)
