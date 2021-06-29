from celery import shared_task

from django.core.mail import send_mail
import requests

from currency.utils import to_decimal, iso_4217_convert, convert_currency_type


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

    available_currency_type = ('USD', 'EUR')
    source = 'privatbank'

    for curr in currencies:
        currency_type = curr['ccy']
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
def parse_monobank():
    from currency.models import Rate

    url = 'https://api.monobank.ua/bank/currency'
    currencies = _get_source_currencies(url)

    available_currency_type = (840, 978)
    basic_currency_type = (980,)
    source = 'monobank'

    for curr in currencies:
        currency_type = curr['currencyCodeA']
        basic_type = curr['currencyCodeB']
        if (
                currency_type in available_currency_type and
                basic_type in basic_currency_type
        ):
            buy = to_decimal(curr['rateBuy'])
            sale = to_decimal(curr['rateSell'])

            # in the selection by the cur_type field, a function for reverse conversion of the currency type
            # has been added, in accordance with the Rate model
            previous_rate = Rate.objects.filter(source=source, cur_type=iso_4217_convert(currency_type)).\
                order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=iso_4217_convert(currency_type),
                    sale=sale,
                    buy=buy,
                    source=source,
                )


@shared_task
def parse_vkurse_dp_ua():
    from currency.models import Rate

    url = 'http://vkurse.dp.ua/course.json'
    currencies = _get_source_currencies(url)

    available_currency_type = ('Dollar', 'Euro')
    source = 'vkurse.dp.ua'

    for key, val in currencies.items():
        currency_type = key
        if key in available_currency_type:
            buy = to_decimal(val['buy'])
            sale = to_decimal(val['sale'])

            # in the selection by the cur_type field, a function for reverse conversion of the currency type
            # has been added, in accordance with the Rate model
            previous_rate = Rate.objects.filter(source=source, cur_type=convert_currency_type(currency_type)).\
                order_by('created').last()
            # check if new rate should be create
            if (
                    previous_rate is None or  # rate does not exists, create first one
                    previous_rate.sale != sale or  # check if sale was changed after last check
                    previous_rate.buy != buy
            ):
                Rate.objects.create(
                    cur_type=convert_currency_type(currency_type),
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
