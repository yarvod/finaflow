import uuid

from django.contrib.auth.models import AbstractUser, UserManager, Group
from django.db import models


class CustomUserManager(UserManager):
    def create_user(self, **kwargs):
        email = kwargs.pop("email")
        password = kwargs.pop("password")
        is_active = kwargs.pop("is_active", True)
        kwargs.pop("username", email)

        user = self.model(email=email, username=email, is_active=is_active, **kwargs)
        user.set_password(password)

        user.save(using=self._db)

        return user


class User(AbstractUser):
    id = models.UUIDField(
        primary_key=True, default=uuid.uuid4, unique=True, editable=False
    )
    username = models.CharField(max_length=150, null=True, blank=True)
    email = models.EmailField(null=True, unique=True)
    phone_number = models.CharField(max_length=17, blank=True, null=True)
    receive_notifications = models.BooleanField(default=True)

    objects = CustomUserManager()

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = ["username", "first_name", "last_name"]

    def __str__(self):
        return f"User(id={self.id}, email={self.email})"

    __repr__ = __str__


class CustomGroup(Group):
    class Meta:
        proxy = True
        verbose_name = "Группа пользователей"
        verbose_name_plural = "Группы пользователей"
