from django.urls import path
from .views import (
    EmailPasswordLoginView,
    LogoutView,
    CookieTokenRefreshView,
    GoogleLoginView,
    YandexLoginView,
    RegisterView,
    EmailActivationView,
    EmailResendActivationView,
    ConfirmResetPasswordView,
    ResetPasswordView,
    CheckEmailView,
)

urlpatterns = [
    path("login/", EmailPasswordLoginView.as_view(), name="login"),
    path('login/social/google', GoogleLoginView.as_view(), name='google-login'),
    path('login/social/yandex', YandexLoginView.as_view(), name='yandex-login'),
    path("logout/", LogoutView.as_view(), name="logout"),
    path("token/refresh/", CookieTokenRefreshView.as_view(), name="refresh"),
    path("register/", RegisterView.as_view(), name="register"),
    path("activate/", EmailActivationView.as_view(), name="activate"),
    path(
        "activate/resend/", EmailResendActivationView.as_view(), name="activate-resend"
    ),
    path("password/reset/", ResetPasswordView.as_view(), name="password-reset"),
    path(
        "password/reset/confirm/",
        ConfirmResetPasswordView.as_view(),
        name="password-reset-confirm",
    ),
    path("check_email/", CheckEmailView.as_view()),
]
