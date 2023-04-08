from django.urls import path, re_path
from users.views import UserMeView

urlpatterns = [
    path("all/", UserMeView.as_view({"get": "list"}), name="all"),
    re_path(
        r"(?P<email>[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+)$",
        UserMeView.as_view({"get": "retrieve"}),
        name="get_email",
    ),
    re_path(
        r"(?P<username>[\w.-]{1,150})$",
        UserMeView.as_view({"get": "retrieve"}),
        name="get_username",
    ),
    path(
        "",
        UserMeView.as_view(
            {"get": "retrieve", "post": "create", "put": "partial_update"}
        ),
        name="me",
    ),
]
