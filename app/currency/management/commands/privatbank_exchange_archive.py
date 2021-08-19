import datetime
from datetime import datetime as dt
from time import sleep

from currency import choices, consts
from currency.models import Rate, Source
from currency.utils import to_decimal

from django.core.management.base import BaseCommand

import requests


def convert_created_db_date(currency_date):
    # date for inserting to model.Rate in created field
    created_db_date = dt.strptime(currency_date, "%d.%m.%Y")
    created_db_date = f'{created_db_date}.000001'
    return created_db_date


def date_start_to_str(date_start):
    # convert date to string for url params
    string_date = date_start.strftime('%d.%m.%Y')
    return string_date


def latest_archive_rates():
    # rate = Rate.objects.filter(bank='1').order_by('created')
    # rate.created.time()
    # for rates in rate:
    #     if rates.created.time() == datetime.time(0, 0, 0, 1):
    #         a = []
    #         a.append(rates)

    # rate = Rate.objects.filter(bank='1', created.time()==datetime.time(0, 0, 0, 1)).last()

    # return latest_data_start
    pass


class Command(BaseCommand):
    help = 'parse exchange archive from PrivatBank'  # noqa

    def handle(self, *args, **options):
        date_start = datetime.date(2014, 12, 1)
        # date_stop = datetime.date(2014, 12, 18)
        date_stop = dt.now().date()

        available_currency_type = {
            'USD': choices.RATE_TYPE_USD,
            'EUR': choices.RATE_TYPE_EUR,
        }

        while True:
            date_parse = f'json&date={date_start_to_str(date_start)}'
            url = 'https://api.privatbank.ua/p24api/exchange_rates'
            response = requests.get(url, params=date_parse)
            response.raise_for_status()

            currency_list = response.json()['exchangeRate']
            currency_date = response.json()['date']

            for curr in currency_list:
                currency_type = curr['currency']
                if currency_type in available_currency_type:
                    currency_type = available_currency_type[curr['currency']]
                    buy = to_decimal(curr['purchaseRate'])
                    sale = to_decimal(curr['saleRate'])
                    bank = Source.objects.get(code_name=consts.CODE_NAME_PRIVATBANK)

                    previous_rate = Rate.objects.filter(
                        created=convert_created_db_date(currency_date),
                        bank=bank,
                        cur_type=currency_type
                    ).order_by('created').last()

                    # check if new rate should be create
                    if (
                            previous_rate is None or  # rate does not exists, create first one
                            previous_rate.sale != sale or  # check if sale was changed after last check
                            previous_rate.buy != buy
                    ):
                        # create Rate object
                        Rate.objects.create(
                            cur_type=currency_type,
                            sale=sale,
                            buy=buy,
                            bank=bank,
                        )

                        # update created field before create Rate object
                        rate = Rate.objects.last()
                        Rate.objects.filter(id=rate.id).update(created=convert_created_db_date(currency_date))

            if date_start == date_stop:
                break
            date_start += datetime.timedelta(days=1)
            sleep(6)
