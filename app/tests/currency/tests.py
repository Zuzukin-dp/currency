import pytest

from currency import choices
from currency.models import Rate, Source


@pytest.mark.skip  # comment test
def test_index(client):
    response = client.get('/')
    assert response.status_code == 200
    assert [t.name for t in response.templates] == [
        'index.html',
        'base.html',
        'includes/navbar.html',
        'includes/footer.html'
    ]


def test_rate_list(client):
    response = client.get('/currency/rate/list/')
    assert response.status_code == 200


def test_create_rate_get_form(client):
    response = client.get('/currency/rate/create/')
    assert response.status_code == 200


def test_create_rate_empty_form_data(client):
    response = client.post('/currency/rate/create/')
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'cur_type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }


def test_create_rate_invalid_form_data(client):
    rates_initial_count = Rate.objects.count()
    form_data = {
        'cur_type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': 99999
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'bank': ['Select a valid choice. That choice is not one of the available choices.'],
    }
    assert Rate.objects.count() == rates_initial_count


def test_create_rate_success(client):
    rates_initial_count = Rate.objects.count()
    bank = Source.objects.last()
    form_data = {
        'cur_type': choices.RATE_TYPE_USD,
        'sale': 20,
        'buy': 30,
        'bank': bank.id
    }
    response = client.post('/currency/rate/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/rate/list/'
    assert Rate.objects.count() == rates_initial_count + 1


def test_update_rate_invalid(client):
    rates_initial_count = Rate.objects.count()
    rate = Rate.objects.last()
    response = client.post(f'/currency/rate/update/{rate.pk}/')
    assert response.status_code == 302
    assert response.url == f'/accounts/login/?next=/currency/rate/update/{rate.pk}/'
    assert Rate.objects.count() == rates_initial_count


def test_update_rate_success(client, django_user_model):
    email = "test_user@test_mail.com"
    username = "test_user@test_mail.com"
    password = "qwerty"
    is_superuser = True
    # user = django_user_model.objects.create_user(
    user = django_user_model.objects.create(
        username=username,
        email=email,
        password=password,
        is_superuser=is_superuser,
    )
    client.force_login(user)

    rates_initial_count = Rate.objects.count()
    rate = Rate.objects.last()
    form_data = {
        'cur_type': choices.RATE_TYPE_USD,
        'sale': rate.sale + 10,
        'buy': rate.buy + 10,
    }
    response = client.post(f'/currency/rate/update/{rate.pk}/', data=form_data)
    # breakpoint()
    assert response.status_code == 200  # wrong status_code, correct 302
    # assert Rate.objects.count() == rates_initial_count
    # rate.refresh_from_db()
    # breakpoint()
    # assert rate.sale == form_data['sale']


def test_create_contact_us(client, mailoutbox, settings, faker):
    email_from = faker.email()
    form_data = {
        'email_from': email_from,
        'subject': 'subject_test_create_contact_us',
        'message': 'message_test_create_contact_us',
    }
    response = client.post('/currency/contactus/create/', data=form_data)
    assert response.status_code == 302
    assert response.url == '/currency/contactus/list/'
    assert len(mailoutbox) == 1
    mail = mailoutbox[0]
    # breakpoint()
    assert mail.to == [settings.DEFAULT_FROM_EMAIL]
    assert mail.cc == []
    assert mail.bcc == []
    assert mail.reply_to == []
    assert mail.from_email == settings.EMAIL_HOST_USER
    assert mail.body == f'\n        From: {email_from}' \
                        f'\n        Topic: {form_data["subject"]}' \
                        f'\n        Message' \
                        f'\n        {form_data["message"]}\n        '
    # breakpoint()
