from django.utils import timezone
from rest_framework_simplejwt.authentication import JWTAuthentication
from django.conf import settings

from rest_framework.authentication import CSRFCheck
from rest_framework import exceptions

import logging

from rest_framework_simplejwt.exceptions import InvalidToken, TokenError
from rest_framework_simplejwt.settings import api_settings

from authentication.services import get_user_hash

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
    from rest_framework_simplejwt.settings import api_settings as jwt_settings

    response.set_cookie(
        key=getattr(settings, "JWT_AUTH_COOKIE", None),
        value=serializer_data["access"],
        expires=(timezone.now() + jwt_settings.ACCESS_TOKEN_LIFETIME),
        secure=getattr(settings, "JWT_AUTH_SECURE", False),
        httponly=getattr(settings, "JWT_AUTH_HTTPONLY", True),
        samesite=getattr(settings, "JWT_AUTH_SAMESITE", "Lax"),
        path=getattr(settings, "JWT_AUTH_COOKIE_PATH", "/"),
    )
    response.set_cookie(
        key=getattr(settings, "JWT_AUTH_REFRESH_COOKIE", None),
        value=serializer_data["refresh"],
        expires=(timezone.now() + jwt_settings.REFRESH_TOKEN_LIFETIME),
        secure=getattr(settings, "JWT_AUTH_SECURE", False),
        httponly=getattr(settings, "JWT_AUTH_HTTPONLY", True),
        samesite=getattr(settings, "JWT_AUTH_SAMESITE", "Lax"),
        path=getattr(settings, "JWT_AUTH_REFRESH_COOKIE_PATH", "/"),
    )


class CustomAuthentication(JWTAuthentication):
    def authenticate(self, request):
        header = self.get_header(request)

        if header is None:
            raw_token = request.COOKIES.get(settings.JWT_AUTH_COOKIE) or None
        else:
            raw_token = self.get_raw_token(header)
        if raw_token is None:
            return None

        validated_token = self.get_validated_token(raw_token)
        enforce_csrf(request)
        return self.get_user(validated_token), validated_token

    def get_validated_token(self, raw_token):
        messages = []
        for AuthToken in api_settings.AUTH_TOKEN_CLASSES:
            try:
                check_token = AuthToken(raw_token)
                exists = get_user_hash(user_id=check_token.payload["user_id"])
                if exists == check_token.payload["hash"]:
                    return check_token
                else:
                    raise InvalidToken(
                        {
                            "detail": "Token not found in database",
                        }
                    )
            except TokenError as e:
                messages.append(
                    {
                        "token_class": AuthToken.__name__,
                        "token_type": AuthToken.token_type,
                        "message": e.args[0],
                    }
                )

        raise InvalidToken(
            {
                "detail": "Given token not valid for any token type",
                "messages": messages,
            }
        )
