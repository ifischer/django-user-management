import pytest
from django.contrib.auth.models import User
from django.urls import reverse

from rest_framework.test import APIClient


@pytest.fixture(scope="class")
def client():
    user = User.objects.create_user(username="testuser", email="testuser@test.com")
    user.save()
    client = APIClient()
    client.force_authenticate(user)
    return client


class TestUserManagement:
    @pytest.mark.django_db
    def test_import_files_to_db(self, client):
        url = reverse(viewname="users")
        response = client.get(url)
        assert response.status_code == 200

    @pytest.mark.django_db
    def test_add_user(self, client):
        url = reverse(viewname="users")
        response = client.post(
            url, data={"username": "testuser", "email": "foo@bar.de"}
        )
        assert response.status_code == 200
        assert User.objects.exists()
