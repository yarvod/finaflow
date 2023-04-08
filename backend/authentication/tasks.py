import logging

from django.contrib.auth.tokens import default_token_generator
from django.conf import settings

from api.utils import send_mail
from backend_app.celery import app
from users.models import User

logger = logging.getLogger(__name__)


@app.task
def send_activation_email(to_email: str):
    logger.info(msg=f"Start send Email verification to {to_email}")
    subject = "Account Activation on phystech-job.ru"
    try:
        user = User.objects.get(email=to_email)
    except User.DoesNotExist:
        logger.info(f"User with email {to_email} NOT FOUND")
        return None
    token = default_token_generator.make_token(user)
    url = settings.EMAIL_ACTIVATION_URL.format(uid=user.id, token=token)
    html_content = f"""To activate account go {url}"""  # TODO: need pretty template
    send_mail(subject=subject, to=to_email, body=html_content)
    logger.info(msg=f"Email verification code {token} send to {to_email}")
    return True


@app.task
def send_password_reset_email(to_email: str):
    logger.info(msg=f"Start send Email password reset to {to_email}")
    subject = "Password reset on phystech-job.ru"
    try:
        user = User.objects.get(email=to_email)
    except User.DoesNotExist:
        logger.info(f"User with email {to_email} NOT FOUND")
        return None
    token = default_token_generator.make_token(user)
    url = settings.EMAIL_RESET_PASSWORD_URL.format(uid=user.id, token=token)
    html_content = f"""To reset password go {url}"""  # TODO: need pretty template
    send_mail(subject=subject, to=to_email, body=html_content)
    logger.info(msg=f"Email password reset code {token} send to {to_email}")
