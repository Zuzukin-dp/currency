# Generated by Django 3.2.3 on 2021-07-06 20:28

from django.db import migrations
# from currency.models import Rate wrong


def forwards(apps, schema_editor):
    Rate = apps.get_model('currency', 'Rate')
    for rate in Rate.objects.all():
        rate.cur_type_new = 11 if 'EUR' in rate.cur_type else 10
        rate.save()


def backwards(apps, schema_editor):
    print('HELLO FROM BACKWARDS')


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0009_alter_rate_cur_type_new'),
    ]

    operations = [
        migrations.RunPython(forwards, backwards),
    ]
