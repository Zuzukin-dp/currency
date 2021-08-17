from currency import choices
from currency.models import Rate


def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/rates/')
    assert response.status_code == 200
    assert 'results' in response.json()


def test_create_rates_invalid(client_api_auth):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.post('/api/rates/', data={})
    assert response.status_code == 400
    assert response.json() == {
        'buy': ['This field is required.'],
        'sale': ['This field is required.'],
        'cur_type': ['This field is required.'],
        'bank': ['This field is required.']
    }
    assert Rate.objects.count() == rates_initial_count


def test_create_rates_success(client_api_auth, bank):
    rates_initial_count = Rate.objects.count()
    form_data = {
        'cur_type': choices.RATE_TYPE_USD,
        'sale': 29.99,
        'buy': 28.99,
        'bank': bank.id
    }
    response = client_api_auth.post('/api/rates/', data=form_data)
    assert response.status_code == 201
    assert response.json()['id'] == response.data['id']
    assert response.json()['cur_type'] == form_data['cur_type']
    assert response.json()['sale'] == str(form_data['sale'])
    assert response.json()['buy'] == str(form_data['buy'])
    assert response.json()['bank_object']['id'] == form_data['bank']
    assert Rate.objects.count() == rates_initial_count + 1


def test_update_rates_invalid(client_api_auth, rate):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.put(f'/api/rates/{rate.id}/')

    assert response.status_code == 400
    assert response.json() == {
        'cur_type': ['This field is required.'],
        'sale': ['This field is required.'],
        'buy': ['This field is required.'],
        'bank': ['This field is required.']
    }
    assert Rate.objects.count() == rates_initial_count


def test_rates_update_put_success(client_api_auth, rate, bank):
    rates_initial_count = Rate.objects.count()
    data = {
        'cur_type': choices.RATE_TYPE_USD,
        'sale': rate.sale + 10,
        'buy': rate.buy + 10,
        'bank': bank.id
    }
    response = client_api_auth.put(f'/api/rates/{rate.id}/', data=data)
    assert response.status_code == 200
    assert response.json()['id'] == rate.id
    rate.refresh_from_db()
    assert response.json()['cur_type'] == rate.cur_type
    assert response.json()['sale'] == str(rate.sale)
    assert response.json()['buy'] == str(rate.buy)
    assert response.json()['bank'] == bank.id
    assert Rate.objects.count() == rates_initial_count


def test_rates_update_patch_success(client_api_auth, rate, bank):
    rates_initial_count = Rate.objects.count()
    data = {
        'buy': rate.buy + 10
    }
    response = client_api_auth.patch(f'/api/rates/{rate.id}/', data=data)
    assert response.status_code == 200
    assert response.json()['id'] == rate.id
    rate.refresh_from_db()
    assert response.json()['cur_type'] == rate.cur_type
    assert response.json()['sale'] == str(rate.sale)
    assert response.json()['buy'] == str(rate.buy)
    assert response.json()['bank'] == bank.id
    assert Rate.objects.count() == rates_initial_count


def test_rates_delete(client_api_auth, rate):
    rates_initial_count = Rate.objects.count()
    response = client_api_auth.delete(f'/api/rates/{rate.id}/')
    assert response.status_code == 204
    assert response.request['REQUEST_METHOD'] == 'DELETE'
    assert Rate.objects.count() == rates_initial_count - 1
