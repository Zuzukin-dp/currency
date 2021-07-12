# Generated by Django 3.2.3 on 2021-07-12 19:34

from django.db import migrations


def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    Source = apps.get_model('currency', 'Source')

    privatbank = Source.objects.create(
        name='PrivatBank',
        url='https://api.privatbank.ua/p24api/pubinfo?json&exchange&coursid=5',
        original_url='https://privatbank.ua/',
        phone='3700'
    )

    monobank = Source.objects.create(
        name='MonoBank',
        url='https://api.monobank.ua/bank/currency',
        original_url='https://www.monobank.ua/',
        phone='0 800 205 205'
    )

    vkurse = Source.objects.create(
        name='Vkurse',
        url='http://vkurse.dp.ua/course.json',
        original_url='http://vkurse.dp.ua/',
        phone='+38(067)989-22-95'
    )

    oschadbank = Source.objects.create(
        name='OschadBank',
        url='https://www.oschadbank.ua/ua',
        original_url='https://www.oschadbank.ua/ua',
        phone='0 800 210 800'
    )

    alfabank = Source.objects.create(
        name='AlfaBank',
        url='https://alfabank.ua/',
        original_url='https://alfabank.ua/',
        phone='3344'
    )

    raiffeisen = Source.objects.create(
        name='RaiffeisenBank',
        url='https://raiffeisen.ua/',
        original_url='https://raiffeisen.ua/',
        phone='0 800 500 500'
    )

    for rate in Rate.objects.all():
        if 'privatbank' in rate.source.lower():
            rate.bank = privatbank
        elif 'monobank' in rate.source.lower():
            rate.bank = monobank
        elif 'vkurse.dp.ua' in rate.source.lower():
            rate.bank = vkurse
        elif 'oschadbank' in rate.source.lower():
            rate.bank = oschadbank
        elif 'alfabank' in rate.source.lower():
            rate.bank = alfabank
        elif 'raiffeisen' in rate.source.lower():
            rate.bank = raiffeisen

        rate.save()


def backwards(apps, schema_editor):
    print('HELLO FROM BACKWARDS') # noqa


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0018_rate_bank'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]