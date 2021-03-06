import random
import string
from decimal import Decimal

from currency import choices
from currency import consts
from currency.models import Rate, Source

from django.core.cache import cache
# import requests
# import csv
# from faker import Faker


def generate_password(length: int = 10) -> str:

    chars = string.ascii_letters + string.digits
    password = ''

    for _ in range(length):
        password += random.choice(chars)

    return password


def read_txt(name: str = 'requirements.txt') -> str:
    with open(name, "r") as txt_file:
        return txt_file.read()


def to_decimal(number: str) -> Decimal:
    """
    :inputs number as string:
    :returns a number as a string, rounded to two decimal places:
    """
    if ',' in str(number):
        number = number.replace(',', '.')
    return Decimal(number).quantize(Decimal('0.01'))


def iso_4217_convert(curr_type: any) -> str:
    """
    function converts letter or digital code in accordance with the international standard ISO 4217.
    :return letter or digital code -> str:
    """

    dict_iso_4217 = {
                    '959': 'XAU',
                    '840': 'USD',
                    '978': 'EUR',
                    '980': 'UAH',
                    '985': 'PLN',
                    }
    for key, val in dict_iso_4217.items():
        if str(curr_type) in key:
            return val
        elif str(curr_type) in val:
            return str(key)

    return f'{curr_type} not in dict ISO 4217'


def convert_currency_type(curr_type: str) -> str:
    """
    the function converts a non-standard currency type,
    the dictionary can be supplemented
    """
    currency_dict = {
        'Dollar': 'USD',
        'Euro': 'EUR',
    }
    for key, val in currency_dict.items():
        if str(curr_type) in key:
            return val
        elif str(curr_type) in val:
            return str(key)

    return f'{curr_type} not in currency_dict'


def get_latest_rates():

    # cache implemented as a class, @method_decorator(cache_page(60 * 60 * 8), name='dispatch')
    if consts.CACHE_KEY_LATEST_RATES in cache:
        return cache.get(consts.CACHE_KEY_LATEST_RATES)

    # context['object_list'] = []
    object_list = []

    for source in Source.objects.all():
        for currency_type, _ in choices.RATE_TYPE_CHOICES:
            latest_rate = Rate.objects \
                    .filter(cur_type=currency_type, bank=source) \
                    .order_by('-created').first()
            if latest_rate is not None:
                object_list.append(latest_rate)

    # cache implemented as a class, @method_decorator(cache_page(60 * 60 * 8), name='dispatch')
    cache.set(consts.CACHE_KEY_LATEST_RATES, object_list, 60 * 60 * 8)

    return object_list
