from rest_framework import serializers
from currency.models import Rate, Source


class SourceSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'original_url',
            'created',
        )


class RateObjectSerializer(serializers.ModelSerializer):

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


class SourceDetailsSerializer(serializers.ModelSerializer):
    rates_set = RateObjectSerializer(source='id', many=True)

    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'url',
            'original_url',
            'phone',
            'created',
            'updated',
            'source_logo',
            'rates_set',
        )


class SourceObjectSerializer(serializers.ModelSerializer):
    class Meta:
        model = Source
        fields = (
            'id',
            'name',
            'code_name',
        )


class RateSerializer(serializers.ModelSerializer):
    bank_object = SourceObjectSerializer(source='bank', read_only=True)

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
