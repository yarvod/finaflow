import logging
from allauth.socialaccount.providers.google.views import GoogleOAuth2Adapter
from allauth.socialaccount.providers.oauth2.client import OAuth2Client, OAuth2Error
from allauth.socialaccount.providers.yandex.views import YandexAuth2Adapter
from dj_rest_auth.registration.serializers import SocialLoginSerializer
from dj_rest_auth.registration.views import SocialLoginView
from django.core.exceptions import BadRequest
from rest_framework.generics import CreateAPIView
from rest_framework_simplejwt.exceptions import TokenError, InvalidToken
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView

from django.middleware import csrf
from rest_framework.views import APIView
from rest_framework.response import Response
from django.conf import settings
from rest_framework import status
from rest_framework.permissions import IsAuthenticated, AllowAny

from users.models import User
from .authenticate import set_cookies, CustomAuthentication
from .serializers import (
    CookieTokenRefreshSerializer,
    CookieTokenObtainSerializer,
    CustomEmailPassSerializer,
    RegisterSerializer,
    EmailActivationSerializer,
    EmailSendSerializer,
    ResetPasswordSerializer,
    EmailSendSerializerWithCreation,
    CheckEmailSerializer,
)

from .services import delete_hash
from authentication import tasks

logger = logging.getLogger()
logger.setLevel(logging.DEBUG)
debug = logger.debug


class LoginView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = CookieTokenObtainSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = Response(status=200)
        set_cookies(response, serializer.validated_data)
        csrf.get_token(request)
        return response


class EmailPasswordLoginView(LoginView):
    serializer_class = CustomEmailPassSerializer


class RegisterView(CreateAPIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    queryset = User.objects.all()
    serializer_class = RegisterSerializer

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        tasks.send_activation_email.apply_async(
            kwargs=dict(to_email=serializer.validated_data["email"])
        )
        headers = self.get_success_headers(serializer.data)
        return Response(
            serializer.data, status=status.HTTP_201_CREATED, headers=headers
        )


class EmailActivationView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = EmailActivationSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.instance
        user.is_active = True
        user.save()

        return Response(status=status.HTTP_200_OK, data={"status": "activated"})


class EmailResendActivationView(APIView):
    permission_classes = ()
    authentication_classes = ()
    serializer_class = EmailSendSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tasks.send_activation_email.apply_async(
            kwargs=dict(to_email=serializer.validated_data["email"])
        )

        return Response(
            status=status.HTTP_200_OK, data={"status": "activation email resent"}
        )


class ConfirmResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = EmailSendSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        tasks.send_password_reset_email.apply_async(
            kwargs=dict(to_email=serializer.validated_data["email"])
        )

        return Response(
            status=status.HTTP_200_OK, data={"status": "reset password email sent"}
        )


class ResetPasswordView(APIView):
    permission_classes = (AllowAny,)
    authentication_classes = ()
    serializer_class = ResetPasswordSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(status=status.HTTP_200_OK, data={"status": "new password set"})


class LogoutView(APIView):
    authentication_classes = (CustomAuthentication,)
    permission_classes = (IsAuthenticated,)

    def post(self, request, *args, **kwargs):
        delete_hash(user_id=str(request.user.id))
        response = Response(status=status.HTTP_205_RESET_CONTENT)
        response.delete_cookie(
            key=settings.JWT_AUTH_REFRESH_COOKIE,
            path=settings.JWT_AUTH_REFRESH_COOKIE_PATH,
        )
        response.delete_cookie(settings.JWT_AUTH_COOKIE)
        return response


class CookieTokenRefreshView(TokenRefreshView):
    authentication_classes = (CustomAuthentication,)

    def get_serializer_class(self):
        return CookieTokenRefreshSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])
        response = Response(data=serializer.validated_data, status=200)
        set_cookies(response, serializer.validated_data)
        return response


class CustomSocialLoginView(SocialLoginView):
    authentication_classes = ()
    permission_classes = ()

    serializer_class = SocialLoginSerializer

    def post(self, request, *args, **kwargs):
        self.request = request
        self.serializer = self.get_serializer(data=self.request.data)
        try:
            self.serializer.is_valid(raise_exception=True)
        except (BadRequest, OAuth2Error) as e:
            return Response(data=f"{e}", status=400)
        self.login()
        return self.get_response()


class GoogleLoginView(CustomSocialLoginView):
    adapter_class = GoogleOAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.GOOGLE_OAUTH2_REDIRECT


class YandexLoginView(CustomSocialLoginView):
    adapter_class = YandexAuth2Adapter
    client_class = OAuth2Client
    callback_url = settings.YANDEX_OAUTH2_REDIRECT


class CheckEmailView(APIView):
    authentication_classes = ()
    permission_classes = ()

    def post(self, request):
        serializer = CheckEmailSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = User.objects.filter(email=serializer.validated_data.get("email")).first()
        return Response(data={"exists": bool(user)}, status=200)
