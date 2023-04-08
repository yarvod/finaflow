from hashlib import sha256

import jwt
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from jwt import DecodeError
from rest_framework import serializers
from rest_framework.exceptions import ValidationError
from rest_framework.validators import UniqueValidator
from rest_framework_simplejwt.serializers import (
    TokenRefreshSerializer,
    TokenObtainPairSerializer,
)
from rest_framework_simplejwt.exceptions import TokenError

from authentication.services import (
    gen_random_string,
    set_hash_with_ttl,
    get_user_hash,
    delete_hash,
)
from users.models import User
from users.serializers import UserREADSerializer


class CookieTokenObtainSerializer(TokenObtainPairSerializer):
    @classmethod
    def get_token(cls, user):
        token = super().get_token(user)
        rand_str = gen_random_string(32)
        token["hash"] = sha256(str(f"{user.id};{rand_str}").encode("utf-8")).hexdigest()
        ttl = int(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds())
        set_hash_with_ttl(user_id=str(user.id), my_hash=token["hash"], ttl=ttl)
        return token

    def validate(self, data):
        refresh = self.get_token(data["id"])
        data["refresh"] = str(refresh)
        data["access"] = str(refresh.access_token)
        data["user"] = UserREADSerializer().to_representation(data["id"])
        data.pop("id")
        return data


class CustomEmailPassSerializer(CookieTokenObtainSerializer):
    password = serializers.CharField(max_length=128, required=True)

    def validate(self, data):
        user = User.objects.filter(
            email=self.initial_data["email"], is_active=True
        ).first()
        try:
            data["id"] = str(user.id)
            return super(CookieTokenObtainSerializer, self).validate(data)
        except AttributeError:
            raise serializers.ValidationError("No such user")


class CookieTokenRefreshSerializer(TokenRefreshSerializer):
    refresh = serializers.CharField(required=False)

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        if attrs["refresh"]:
            old_refresh = attrs["refresh"]
            try:
                old_token = jwt.decode(
                    old_refresh,
                    settings.SIMPLE_JWT["SIGNING_KEY"],
                    algorithms=settings.SIMPLE_JWT["ALGORITHM"],
                )
            except DecodeError:
                raise TokenError("Token not correctly decoded or not found in cookie")
            if get_user_hash(user_id=old_token["user_id"]) == old_token["hash"]:
                new_token = self.token_class(old_refresh)
                data = {"access": str(new_token.access_token)}
                if settings.SIMPLE_JWT["ROTATE_REFRESH_TOKENS"]:
                    new_token.set_jti()
                    new_token.set_exp()
                    new_token.set_iat()
                    data["refresh"] = str(new_token)
                # delete_hash(user_id=old_token['user_id'])
                new_token["hash"] = old_token["hash"]
                ttl = int(settings.SIMPLE_JWT["REFRESH_TOKEN_LIFETIME"].total_seconds())
                set_hash_with_ttl(
                    user_id=str(new_token["user_id"]),
                    my_hash=new_token["hash"],
                    ttl=ttl,
                )
                return data
            else:
                raise TokenError("No such hash in store")
        else:
            raise TokenError("No token found in cookie")


class RegisterSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ("email", "password", "password2", "first_name", "last_name")

    email = serializers.EmailField(
        required=True, validators=[UniqueValidator(queryset=User.objects.all())]
    )

    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    first_name = serializers.CharField()
    last_name = serializers.CharField()

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        if all((attrs.get("employee"), attrs.get("employer"))):
            raise serializers.ValidationError(
                {"employee&employer": "Can't be together."}
            )

        return attrs

    def create(self, validated_data):
        user = User.objects.create_user(
            username=validated_data["email"],
            email=validated_data["email"],
            password=validated_data["password"],
            first_name=validated_data.get("first_name", ""),
            last_name=validated_data.get("last_name", ""),
            is_active=False,
        )

        return user


class EmailSendSerializer(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        try:
            User.objects.get(email=email)
        except User.DoesNotExist:
            raise ValidationError(detail="Not found such user", code=404)

        return attrs


class EmailSendSerializerWithCreation(serializers.Serializer):
    email = serializers.EmailField(required=True)

    def validate(self, attrs):
        email = attrs.get("email")
        User.objects.get_or_create(email=email)
        return attrs


class UidAndTokenSerializer(serializers.Serializer):
    uid = serializers.CharField()
    token = serializers.CharField()

    default_error_messages = {
        "invalid_token": "Invalid Token",
        "invalid_uid": "Invalid UID",
    }

    def validate(self, attrs):
        validated_data = super().validate(attrs)
        try:
            uid = self.initial_data.get("uid", "")
            self.company_uid = self.initial_data.get("company_uid", "")
            self.instance = User.objects.get(pk=uid)
            self.instance.is_active = True
            self.instance.save()
        except (User.DoesNotExist, ValueError, TypeError, OverflowError):
            key_error = "invalid_uid"
            raise ValidationError(
                {"uid": [self.error_messages[key_error]]}, code=key_error
            )

        is_token_valid = default_token_generator.check_token(
            self.instance, self.initial_data.get("token", "")
        )
        if is_token_valid:
            return validated_data
        else:
            key_error = "invalid_token"
            raise ValidationError(
                {"token": [self.error_messages[key_error]]}, code=key_error
            )


class EmailActivationSerializer(UidAndTokenSerializer):
    pass


class ResetPasswordSerializer(UidAndTokenSerializer):
    password = serializers.CharField(
        write_only=True, required=True, validators=[validate_password]
    )
    password2 = serializers.CharField(write_only=True, required=True)

    def validate(self, attrs):
        if attrs["password"] != attrs["password2"]:
            raise serializers.ValidationError(
                {"password": "Password fields didn't match."}
            )

        super().validate(attrs)

        return attrs

    def update(self, instance, validated_data):
        instance.set_password(validated_data["password"])
        instance.save()
        return instance


class CheckEmailSerializer(serializers.Serializer):
    email = serializers.EmailField()
