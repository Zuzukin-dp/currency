from currency.tasks import parse_monobank
from currency.models import Source, Rate
from currency import consts
from unittest.mock import MagicMock


def test_parse_monobank(mocker):
    json_mock = lambda: [
        {"currencyCodeA": 840, "currencyCodeB": 980, "date": 1629202806, "rateBuy": 26.6, "rateSell": 26.8003},
        {"currencyCodeA": 978, "currencyCodeB": 980, "date": 1629211206, "rateBuy": 31.25, "rateSell": 31.5996},
    ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))

    code_name = consts.CODE_NAME_MONOBANK
    monobank_data = {
        'name': 'MonoBank',
        'url': 'https://api.monobank.ua/bank/currency',
        'original_url': 'https://www.monobank.ua/',
    }
    Source.objects.create(code_name=code_name, **monobank_data)

    initial_count = Rate.objects.count()
    parse_monobank()

    assert Rate.objects.count() == initial_count + 2
