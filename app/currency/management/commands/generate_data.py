from django.core.management.base import BaseCommand, CommandError
from currency.models import Rate


class Command(BaseCommand):
    help = 'Generate Random records'

    def handle(self, *args, **options):
        for i in range(300):
            Rate.objects.create(
                cur_type='',
                sale='',
                buy='',
                source='',
            )
