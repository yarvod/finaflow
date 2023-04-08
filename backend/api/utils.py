import logging

from django.core.mail import EmailMessage


logger = logging.getLogger(__name__)


def send_mail(subject, to, body):
    msg = EmailMessage(subject=subject, body=body, to=[to])
    msg.content_subtype = "html"
    msg.send()
    logger.info(f"Email sent to {to}")
