from rest_framework import serializers
from currency.models import Rate


class RateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'cur_type',
            'cur_type',
            'bank',
        )


class RateDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'cur_type',
            'cur_type',
            'bank',
        )
