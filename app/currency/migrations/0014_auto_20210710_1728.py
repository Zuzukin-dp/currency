# Generated by Django 3.2.3 on 2021-07-10 17:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0013_analytics'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='analytics',
            name='reuest_method',
        ),
        migrations.AddField(
            model_name='analytics',
            name='status',
            field=models.PositiveSmallIntegerField(default=1),
            preserve_default=False,
        ),
    ]
