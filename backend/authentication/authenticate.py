import jwt
from django.utils import timezone
from django.conf import settings

from rest_framework.authentication import CSRFCheck, BaseAuthentication
from rest_framework import exceptions

import logging

from users.models import User

logger = logging.getLogger(__name__)
logger.setLevel(logging.DEBUG)
debug = logger.debug


def enforce_csrf(request):
    check = CSRFCheck()
    check.process_request(request)
    reason = check.process_view(request, None, (), {})
    if reason:
        raise exceptions.PermissionDenied("CSRF Failed: %s" % reason)


def set_cookies(response, serializer_data):
    response.set_cookie(
        key=getattr(settings, "JWT_AUTH_COOKIE", None),
        value=serializer_data["access"],
        expires=(timezone.now() + settings.ACCESS_TOKEN_LIFETIME),
        secure=getattr(settings, "JWT_AUTH_SECURE", False),
        httponly=getattr(settings, "JWT_AUTH_HTTPONLY", True),
        samesite=getattr(settings, "JWT_AUTH_SAMESITE", "Lax"),
        path=getattr(settings, "JWT_AUTH_COOKIE_PATH", "/"),
    )
    response.set_cookie(
        key=getattr(settings, "JWT_AUTH_REFRESH_COOKIE", None),
        value=serializer_data["refresh"],
        expires=(timezone.now() + settings.REFRESH_TOKEN_LIFETIME),
        secure=getattr(settings, "JWT_AUTH_SECURE", False),
        httponly=getattr(settings, "JWT_AUTH_HTTPONLY", True),
        samesite=getattr(settings, "JWT_AUTH_SAMESITE", "Lax"),
        path=getattr(settings, "JWT_AUTH_REFRESH_COOKIE_PATH", "/"),
    )


class CustomAuthentication(BaseAuthentication):
    def authenticate(self, request):
        authorization_header = request.headers.get("Authorization")

        if not authorization_header:
            return None
        try:
            access_token = authorization_header.split(" ")[1]
            payload = jwt.decode(
                access_token, settings.JWT_SECRET, algorithms=["HS256"]
            )

        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed("Access token expired")
        except IndexError:
            raise exceptions.AuthenticationFailed("Token prefix missing")

        user = User.objects.filter(id=payload["user_id"]).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")

        if not user.is_active:
            raise exceptions.AuthenticationFailed("user is inactive")

        enforce_csrf(request)
        return user, None
