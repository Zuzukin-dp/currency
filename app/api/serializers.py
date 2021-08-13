from rest_framework import serializers
from currency.models import Rate, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'code_name',
        )


class RateSerializer(serializers.ModelSerializer):
    bank_object = SourceSerializer(source='bank', read_only=True)

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'cur_type',
            'bank_object',
            'bank',
        )

        extra_kwargs = {
            'bank': {'write_only': True},
        }


class RateDetailsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Rate
        fields = (
            'id',
            'buy',
            'sale',
            'created',
            'cur_type',
            'bank',
        )
