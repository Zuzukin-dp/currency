import random
from decimal import Decimal

from currency.models import Rate

from django.core.management.base import BaseCommand


def round_to_two(num):
    """
    function rounds value to two decimal places
    """
    return Decimal(num).quantize(Decimal('0.01'))


class Command(BaseCommand):
    help = 'Generate Random records' # noqa

    def handle(self, *args, **options):
        for i in range(300):
            # random value for sale, buy
            rnd_val = random.uniform(20.00, 29.00)

            Rate.objects.create(
                cur_type=random.choice(('usd', 'eur')),
                sale=round_to_two(rnd_val),
                buy=round_to_two(Decimal(rnd_val)/Decimal('1.00358')),
                source=random.choice(['monobank', 'privatbank', 'vkurse']),
            )
