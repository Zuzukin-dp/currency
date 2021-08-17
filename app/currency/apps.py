from django.apps import AppConfig
from django.db import connection


class CurrencyConfig(AppConfig):
    default_auto_field = 'django.db.models.BigAutoField'
    name = 'currency'

    def ready(self):
        from currency.models import Source
        from currency import consts

        all_tables = connection.introspection.table_names()

        # check if table exists
        # table could be absent before initial migration
        # if Source._meta.db_table in all_tables:
        if 'currency_bank' in all_tables:
            # print('Update Banks Initial Data')
            code_name = consts.CODE_NAME_PRIVATBANK
            privatbank_data = {
                'name': 'PrivatBank',
                'url': 'https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
                'original_url': 'https://privatbank.ua',
            }
            Source.objects.update_or_create(code_name=code_name, defaults=privatbank_data)
