from rest_framework import serializers

from .models import User


class UserREADSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "username"]


class UserWRITESerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = ["password", "username"]
