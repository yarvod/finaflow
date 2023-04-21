import jwt
from django.conf import settings
from django.contrib.auth.password_validation import validate_password
from django.contrib.auth.tokens import default_token_generator
from rest_framework import serializers, exceptions
from rest_framework.exceptions import ValidationError
from rest_framework.response import Response
from rest_framework.validators import UniqueValidator

from authentication import services
from users.models import User
from users.serializers import UserREADSerializer


class PasswordField(serializers.CharField):
    def __init__(self, *args, **kwargs):
        kwargs.setdefault("style", {})

        kwargs["style"]["input_type"] = "password"
        kwargs["write_only"] = True

        super().__init__(*args, **kwargs)


class CookieTokenObtainSerializer(serializers.Serializer):
    username_field = User.USERNAME_FIELD
    token_class = None

    default_error_messages = {
        "no_active_account": "No active account found with the given credentials"
    }

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self.fields[self.username_field] = serializers.CharField()
        self.fields["password"] = PasswordField()

    @classmethod
    def get_token(cls, user):
        access_token = services.generate_access_token(user)
        refresh_token = services.generate_refresh_token(user)
        services.set_refresh_token(user_id=user.pk, token=refresh_token)
        return access_token, refresh_token

    def validate(self, data):
        access_token, refresh_token = self.get_token(data["id"])
        data["refresh"] = str(refresh_token)
        data["access"] = str(access_token)
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


class CookieTokenRefreshSerializer(serializers.Serializer):
    access = serializers.CharField(read_only=True)
    refresh = serializers.CharField(required=False)

    def validate(self, attrs):
        attrs["refresh"] = self.context["request"].COOKIES.get("refresh_token")
        try:
            payload = jwt.decode(
                attrs["refresh"], settings.JWT_SECRET, algorithms=["HS256"]
            )
        except jwt.ExpiredSignatureError:
            raise exceptions.AuthenticationFailed(
                "expired refresh token, please login again."
            )
        except jwt.exceptions.DecodeError:
            raise exceptions.AuthenticationFailed("Token is invalid")
        user = User.objects.filter(id=payload.get("user_id")).first()
        if user is None:
            raise exceptions.AuthenticationFailed("User not found")
        if not user.is_active:
            raise exceptions.AuthenticationFailed("User is inactive")
        if services.get_refresh_token(
            user_id=payload.get("user_id"), token=attrs["refresh"]
        ):
            access_token = services.generate_access_token(user)
            new_refresh_token = services.generate_refresh_token(user)
            services.remove_refresh_token(
                user_id=payload.get("user_id"), token=attrs["refresh"]
            )
            services.set_refresh_token(
                user_id=payload.get("user_id"), token=new_refresh_token
            )
            return Response(
                {"AccessToken": access_token, "RefreshToken": new_refresh_token}
            )
        else:
            raise exceptions.AuthenticationFailed("User device not authorized")


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
