from currency.models import ContactUs

from django.core.management.base import BaseCommand

from faker import Faker
fake = Faker()


class Command(BaseCommand):
    help = 'Generate Random records' # noqa

    def handle(self, *args, **options):
        for i in range(300):

            ContactUs.objects.create(
                email_from=fake.email(),
                subject=fake.catch_phrase(),
                message=fake.text(),
            )
