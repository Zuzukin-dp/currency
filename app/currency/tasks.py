import json

from bs4 import BeautifulSoup

from celery import shared_task

from currency.utils import convert_currency_type, iso_4217_convert, to_decimal

from django.core.mail import send_mail

from currency import choices

import requests

# @shared_task
# def print_hallo(object_id):
#     from currency.models import ContactUs
#     ContactUs.objects.get(id=object_id)
#     return f'ContactUs id: {object_id}'


def _get_source_currencies(url):
    response = requests.get(url)
    response.raise_for_status()
    currencies = response.json()
    return currencies


@shared_task
def parse_privatbank():
    from currency.models import Rate

    url = 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5'
    currencies = _get_source_currencies(url)

    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    source = 'privatbank'

    for curr in currencies:
        currency_type = curr['ccy']
        if currency_type in available_currency_type:
            currency_type = available_currency_type[curr['ccy']]
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_monobank():
    from currency.models import Rate

    url = 'https://api.monobank.ua/bank/currency'
    currencies = _get_source_currencies(url)

    available_currency_type = {
        840: choices.RATE_TYPE_USD,
        978: choices.RATE_TYPE_EUR,
    }
    basic_currency_type = (980,)

    source = 'monobank'

    for curr in currencies:
        currency_type = curr['currencyCodeA']
        basic_type = curr['currencyCodeB']
        if (
                currency_type in available_currency_type and
                basic_type in basic_currency_type
        ):
            currency_type = available_currency_type[curr['currencyCodeA']]
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            # in the selection by the cur_type field, a function for reverse conversion of the currency type
            # has been added, in accordance with the Rate model
            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_vkurse_dp_ua():
    from currency.models import Rate

    url = 'http://vkurse.dp.ua/course.json'
    currencies = _get_source_currencies(url)

    available_currency_type = {
        'Dollar': choices.RATE_TYPE_USD,
        'Euro': choices.RATE_TYPE_EUR,
    }

    source = 'vkurse.dp.ua'

    for key, val in currencies.items():
        currency_type = key
        if key in available_currency_type:
            currency_type = available_currency_type[key]
            buy = to_decimal(val['buy'])
            sale = to_decimal(val['sale'])

            # in the selection by the cur_type field, a function for reverse conversion of the currency type
            # has been added, in accordance with the Rate model
            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_oschadbank():
    from currency.models import Rate

    url = 'https://www.oschadbank.ua/ua'
    # parameter to prevent blocking
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='paragraph paragraph--type--exchange-rates '
                                       'paragraph--view-mode--default currency-item', limit=3)

    currencies = []

    for curr in items:
        currencies.append({
            'c_type': curr.find('span', class_='currency-sign').get_text(strip=True),
            # look for a "strong" tag, select by element number, get the "data-buy" value
            'buy': curr.findAll('strong')[0].get_text(strip=True),
            'sale': curr.findAll('strong')[1].get_text(strip=True),
        })

    available_currency_type = {
        'USD': choices.RATE_TYPE_USD,
        'EUR': choices.RATE_TYPE_EUR,
    }

    source = 'oschadbank'

    for curr in currencies:
        currency_type = curr['c_type']
        if currency_type in available_currency_type:
            currency_type = available_currency_type[curr['c_type']]
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_alfabank():
    from currency.models import Rate

    url = 'https://alfabank.ua/'
    # parameter to prevent blocking
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_='currency-block', limit=3)

    currencies = []

    for curr in items:
        currencies.append({
            'c_type': curr.find('div', class_='title').get_text(strip=True),
            # look for a "span" tag, select by element number, get text
            'buy': curr.findAll('span')[1].get_text(strip=True),
            'sale': curr.findAll('span')[3].get_text(strip=True),
        })
    available_currency_type = ('USD', 'EUR')
    source = 'alfabank'

    for curr in currencies:
        currency_type = curr['c_type']
        if currency_type in available_currency_type:
            buy = to_decimal(curr['buy'])
            sale = to_decimal(curr['sale'])

            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_raiffeisen():
    from currency.models import Rate

    url = 'https://raiffeisen.ua/'
    #
    headers = {'User-Agent': 'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit 537.36'
                             '(KHTML, like Gecko) Chrome/91.0.4472.114 Safari/537.36'
               }

    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    items = soup.findAll('div', class_="bank-info__wrap")
    items = items[0].find('currency-table')[':currencies']
    currencies = json.loads(items)

    available_currency_type = ('USD', 'EUR')
    source = 'raiffeisen'

    for curr in currencies:
        currency_type = curr['currency']
        if currency_type in available_currency_type:
            buy = to_decimal(curr['rate_buy'])
            sale = to_decimal(curr['rate_sell'])

            previous_rate = Rate.objects.filter(source=source, cur_type=currency_type).order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=currency_type,
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 30},
)
def task_send_email(body):
    send_mail(
        'Contact Us from Client',
        body,
        'pydjantest@gmail.com',
        ['pydjantest@gmail.com'],
        fail_silently=False,
    )
