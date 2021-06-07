import random

from currency.models import Source

from django.core.management.base import BaseCommand

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Generate Random records' # noqa

    def handle(self, *args, **options):
        for i in range(300):

            Source.objects.create(
                name=random.choice(['privatbank', 'monobank', 'vkurse']),
                url=random.choice(['https://privatbank.ua/', 'https://www.monobank.ua/','http://vkurse.dp.ua/']),
                phone=random.choice(['3700', '0 800 205 205', '+38(067)989-22-95'])
            )
