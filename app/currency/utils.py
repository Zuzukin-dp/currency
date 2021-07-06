import random
import string
from decimal import Decimal

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
