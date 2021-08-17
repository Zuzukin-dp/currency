from currency.tasks import parse_vkurse_dp_ua
from currency.models import Source, Rate
from currency import consts
from unittest.mock import MagicMock


def test_parse_vkurse(mocker):
    json_mock = lambda: {
        "Dollar": {"buy": "26.70", "sale": "26.85"},
        "Euro": {"buy": "31.32", "sale": "31.45"},
    }
    requests_get = mocker.patch('requests.get', return_value=MagicMock(json=json_mock))

    code_name = consts.CODE_NAME_VKURSE
    vkurse_data = {
        'name': 'MonoBank',
        'url': 'http://vkurse.dp.ua/course.json',
        'original_url': 'http://vkurse.dp.ua/',
    }
    Source.objects.create(code_name=code_name, **vkurse_data)

    initial_count = Rate.objects.count()
    parse_vkurse_dp_ua()

    assert Rate.objects.count() == initial_count + 2
