def test_rates_list(client_api_auth):
    response = client_api_auth.get('/api/rates/')
    assert response.status_code == 200
    assert 'results' in response.json()
