
import pytest
from budget_app.models import WalletInstance
from django.contrib.auth import get_user_model


@pytest.mark.django_db
def test_wallet(auth_client, user):

    #print(get_user_model().objects.all())
    #<QuerySet [<User: Dwight>]>
    #user is created but not auth
    


    payload = dict(
        name='wallet_test_name'
    )

    response = auth_client.post('/api/wallet/', payload)


    data = response.data
    status_from_db = WalletInstance.objects.first()

    assert response.status_code == 201

@pytest.mark.django_db
def test_login(user, client):
    # this tests if there is a redirect to auth0 not if is logged correctly
    # how do I test auth0 login with redirect?
     
    response = client.post('/login/auth0', dict(email='shrute@michaelbootlicker.com', password='michael@'))

    assert response.status_code == 302

@pytest.mark.django_db
def test_logout(auth_client):
    response = auth_client.post("/logout/")
    #auth0 redirect 
    assert response.status_code == 302
