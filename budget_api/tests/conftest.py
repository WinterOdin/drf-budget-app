import pytest
from django.conf import settings
from rest_framework. test import APIClient
from django.contrib.auth import get_user_model
from budget_app.models import User
#Testing in this way becouse I do auth0 as my auth 
@pytest.fixture
def user():
    user = User.objects.create(username = 'Dwight',
        last_name = 'Shrute',
        email = 'shrute@michaelbootlicker.com',
        password = 'michael@')

    return user

@pytest.fixture
def client():
    return APIClient()

@pytest.fixture
def auth_client(user, client):
    client.post('/login/auth0', dict(email=user.email, password='michael@'))
    return client