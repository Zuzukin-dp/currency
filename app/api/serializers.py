from currency.models import ContactUs, Rate, Source

from django.conf import settings
from django.core.mail import send_mail

from rest_framework import serializers


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
    rates_set = RateObjectSerializer(source='pk', many=True)

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


class ContactUsSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created',
        )


class ContactUsSendMailSerializer(serializers.ModelSerializer):
    class Meta:
        model = ContactUs
        fields = (
            'id',
            'email_from',
            'subject',
            'message',
            'created',
        )

    def create(self, validate_data):
        # breakpoint()
        instance = super(ContactUsSendMailSerializer, self).create(validate_data)
        send_mail(
            'From Django API created instance {}'.format(instance.pk),
            f'''
            'From': {validate_data['email_from']}
            'Topic': {validate_data['subject']}
            'Message': {validate_data['message']}
            ''',
            settings.EMAIL_HOST_USER,
            [validate_data['email_from']],
            fail_silently=False,
        )
        # breakpoint()
        return instance
