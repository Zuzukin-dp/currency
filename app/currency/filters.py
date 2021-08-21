from currency import choices
from currency.models import Rate, Source

from django.forms import DateInput

import django_filters


class RateFilter(django_filters.FilterSet):
    created_gte = django_filters.DateFilter(
        widget=DateInput(attrs={'type': 'date'}),
        field_name='created', lookup_expr='date__gte',
    )
    created_lte = django_filters.DateFilter(
        widget=DateInput(attrs={'type': 'date'}),
        field_name='created', lookup_expr='date__lte',
    )

    currency_type = django_filters.ChoiceFilter(
        choices=choices.RATE_TYPE_CHOICES,
        field_name='cur_type',
        empty_label='All types',
    )

    source_name = django_filters.ModelChoiceFilter(
        queryset=Source.objects.all().prefetch_related('rate_set').order_by('created'),
        field_name='bank',
        empty_label='All Source',
    )

    class Meta:
        model = Rate
        fields = {
            # 'cur_type': ('currency_type',),
            'buy': ('exact',),
            'sale': ('exact',),
        }
