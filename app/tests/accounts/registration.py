"""
tests need improvement
"""


def test_accounts_signup(client):
    response = client.get('/accounts/signup/')
    assert response.status_code == 200


def test_accounts_signup_post_empty_data(client):
    response = client.post('/accounts/signup/', data={})
    assert response.status_code == 200
    assert response.context['form'].errors == {
        'email': ['This field is required.'],
        'password1': ['This field is required.'],
        'password2': ['This field is required.']
    }


def test_accounts_signup_post_form_data(client, fake):
    form_data = {
        'email': fake.email,
        'password1': 'qwerty123456',
        'password2': 'qwerty123456',
    }
    response = client.post('/accounts/signup/', data=form_data)
    assert response.status_code == 200
    # breakpoint()

