from rest_framework import status
from django.contrib.auth import get_user_model
import pytest

user = get_user_model()


@pytest.fixture
def create_user(api_client):
    def do_create_user(user):
        api_client.post("/v1/auth/login", user)
    return do_create_user()


@pytest.mark.django_db
class TestUsers:
    def test_if_user_is_anonymous_returns_401(self, api_client):
        response = api_client.get("/v1/auth/profile/")
        assert response.status_code == status.HTTP_401_UNAUTHORIZED

    def test_user_is_authenticated_returns_403(self, api_client):
        api_client.force_authenticate(user={})
        response = api_client.get("/v1/auth/profile/")
        assert response.status_code == status.HTTP_403_FORBIDDEN

    def test_invalid_login_user_return_400(self, api_client):
        data = {
            "username": "mohammad",
            "password": "12345678",
            "device_model": "xiaomi",
            "device_os": "android",
            "device_number": "12563254523",
            "ip_address": "127.0.0.1"
        }
        response = api_client.post("/v1/auth/login/", data)
        assert response.status_code == status.HTTP_400_BAD_REQUEST
