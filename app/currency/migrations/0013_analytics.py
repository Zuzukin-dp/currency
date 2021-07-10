# Generated by Django 3.2.3 on 2021-07-10 16:44

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20210707_1926'),
    ]

    operations = [
        migrations.CreateModel(
            name='Analytics',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('path', models.CharField(max_length=255)),
                ('counter', models.PositiveBigIntegerField()),
                ('reuest_method', models.PositiveSmallIntegerField(choices=[(10, 'GET'), (11, 'POST')])),
            ],
        ),
    ]