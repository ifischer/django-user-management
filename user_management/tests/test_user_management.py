import pytest
from django.contrib.auth.models import User
from django.urls import reverse
from django.contrib.auth.models import User
from rest_framework.test import APIClient

#
@pytest.fixture
def user(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        user = User.objects.create_user(username="testuser", email="testuser@test.com")
        user.save()
        return user


@pytest.fixture
def authenticated_client(django_db_setup, django_db_blocker, request, user):
    with django_db_blocker.unblock():
        client = APIClient()
        client.force_authenticate(user)
        request.cls.client = client

#
# @pytest.mark.usefixtures("authenticated_client")
# class TestUserManagement:
#     def test_foo_bar(self):
#         assert True
#
#     @pytest.mark.django_db
#     def test_import_files_to_db(self):
#         url = reverse(viewname="users")
#         response = self.client.get(url)
#         assert response.status_code == 200
#
#     @pytest.mark.django_db
#     def test_add_user(self):
#         url = reverse(viewname="users")
#         response = self.client.post(
#             url, data={"username": "testuser", "email": "foo@bar.de"}
#         )
#         assert response.status_code == 200
#         assert User.objects.exists()

def test_foo():
    assert True

@pytest.mark.django_db
def test_bar():
    User().save()
    print(User.objects.all())


@pytest.mark.django_db
def test_add_user(authenticated_client):
    url = reverse(viewname="users")
    response = authenticated_client.post(
        url, data={"username": "testuser", "email": "foo@bar.de"}
    )
    assert response.status_code == 200
    assert User.objects.exists()
