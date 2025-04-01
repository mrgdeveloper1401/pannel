from rest_framework import serializers

from account_app.models import User


class UserLoginSerializer(serializers.Serializer):
    username = serializers.CharField()
    password = serializers.CharField(write_only=True, style={'input_type': 'password'})
    device_model = serializers.CharField()
    device_os = serializers.CharField()
    device_number = serializers.CharField()
    ip_address = serializers.IPAddressField()
    fcm_token = serializers.CharField(required=False)


class TokenResponseSerializer(serializers.Serializer):
    token = serializers.CharField()


class UserProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        exclude = (
            "id",
            "last_name",
            "is_superuser",
            "groups",
            "user_permissions",
            "created_by",
            "password",
            "is_staff"
        )
