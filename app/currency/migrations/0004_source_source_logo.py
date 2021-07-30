# Generated by Django 3.2.3 on 2021-07-30 20:10

import currency.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0003_alter_analytics_unique_together'),
    ]

    operations = [
        migrations.AddField(
            model_name='source',
            name='source_logo',
            field=models.FileField(blank=True, default=None, null=True, upload_to=currency.models.source_directory_path),
        ),
    ]
