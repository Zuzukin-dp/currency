from unittest.mock import MagicMock

from currency import consts
from currency.models import Rate, Source
from currency.tasks import parse_oschadbank

import pytest


@pytest.mark.skip
def test_parse_privatbank(mocker):
    json_mock = lambda: [  # noqa
        '<div class="paragraph paragraph--type--exchange-rates paragraph--view-mode--default currency-item">'
        '<span class="currency-znak">$</span>'
        '<span class="currency-sign USD"><i></i> USD</span>'
        f'<strong class="buy-USD" data-buy="26.6200"> {26.6200} </strong>'
        '<span class="delimiter">/</span>'
        f'<strong class="sell-USD" data-sell="27.0000"> {27.0000} </strong>'
        '</div>, <div class="paragraph paragraph--type--exchange-rates paragraph--view-mode--default currency-item">'
        '<span class="currency-znak">€</span>'
        '<span class="currency-sign EUR"><i></i> EUR</span>'
        f'<strong class="buy-EUR" data-buy="31.2000"> {31.2000} </strong>'
        '<span class="delimiter">/</span>'
        f'<strong class="sell-EUR" data-sell="31.6800"> {31.6800} </strong>'
        '</div>, <div class="paragraph paragraph--type--exchange-rates paragraph--view-mode--default currency-item">'
        '<span class="currency-znak">₽</span>'
        '<span class="currency-sign RUB"><i></i> RUB</span>'
        f'<strong class="buy-RUB" data-buy="0.2500"> {0.2500} </strong>'
        '<span class="delimiter">/</span>'
        f'<strong class="sell-RUB" data-sell="0.3800"> {0.3800} </strong>'
        '</div>'
        ]
    requests_get = mocker.patch('requests.get', return_value=MagicMock(string=json_mock))  # noqa

    code_name = consts.CODE_NAME_OSCHADBANK
    oschadbank_data = {
        'name': 'OschadBank',
        'url': 'https://www.oschadbank.ua/ua',
        'original_url': 'https://www.oschadbank.ua/ua',
    }
    Source.objects.create(code_name=code_name, **oschadbank_data)

    initial_count = Rate.objects.count()
    parse_oschadbank()

    assert Rate.objects.count() == initial_count + 2
