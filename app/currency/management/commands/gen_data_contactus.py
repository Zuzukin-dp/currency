from django.core.management.base import BaseCommand, CommandError
from currency.models import ContactUs

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for i in range(300):

            ContactUs.objects.create(
                email_from=fake.email(),
                subject=fake.catch_phrase(),
                message=fake.text(),
            )
