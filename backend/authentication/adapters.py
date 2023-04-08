from allauth.account.adapter import DefaultAccountAdapter
from django.core.exceptions import BadRequest


class CustomAccountAdapter(DefaultAccountAdapter):
    def respond_user_inactive(self, request, user):
        raise BadRequest("Account Inactive")  # FIXME: return 400 status directly
