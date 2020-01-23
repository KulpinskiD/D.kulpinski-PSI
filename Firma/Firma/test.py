import pytest

from django.contrib.auth.models import User
from django.urls import *
from Firma import settings

@pytest.mark.django_db
def test_user_create():
  User.objects.create_user('kulpinskid', 'kulpinskid@gmail.com', 'dawid')
  assert User.objects.count() == 1


@pytest.mark.django_db
def test_view(client):
    url = reverse('homepage-url')
    response = client.get(url)
    assert response.status_code == 200