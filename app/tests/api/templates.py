def test_api_list_templates(client):
    response = client.get('/api/api_list/')
    assert response.status_code == 200


def test_api_choices_currency_types_templates(client_api_auth):
    response = client_api_auth.get('/api/choices/currency/types/')
    assert response.status_code == 200
    assert response.json() == [[10, 'Dollar'], [11, 'Euro']]
