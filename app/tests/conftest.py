from django.core.management import call_command

import pytest


@pytest.fixture(autouse=True, scope="function")
def enable_db_access_for_all_tests(db):
    """
    give access to database for all tests
    """


@pytest.fixture(autouse=True, scope="session")
def load_fixture_source(django_db_setup, django_db_blocker):
    with django_db_blocker.unblock():
        call_command('loaddata', 'app/tests/fixtures/source.json')
        call_command('loaddata', 'app/tests/fixtures/rate.json')


@pytest.fixture(autouse=True, scope="function")
def fake():
    from faker import Faker
    faker = Faker()
    yield faker


@pytest.fixture(scope='function')
def client_api_auth(django_user_model):
    from rest_framework.test import APIClient
    client = APIClient()

    email = "test_django_api_usr_auth@example.com"
    password = "qwerty12345678"

    user = django_user_model(email=email)
    user.set_password(password)
    user.save()

    response = client.post('/api/token/', data={'email': email, 'password': password})
    assert response.status_code == 200

    client.credentials(HTTP_AUTHORIZATION='JWT ' + response.json()['access'])

    yield client

    user.delete()


@pytest.fixture(scope='function')
def bank(enable_db_access_for_all_tests):
    from currency.models import Source

    yield Source.objects.last()


@pytest.fixture(scope='function')
def rate(enable_db_access_for_all_tests):
    from currency.models import Rate

    yield Rate.objects.last()
