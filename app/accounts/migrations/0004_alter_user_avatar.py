# Generated by Django 3.2.3 on 2021-07-30 20:10
import accounts.models

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_auto_20210728_1845'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='avatar',
            field=models.FileField(blank=True, default=None, null=True, upload_to=accounts.models.user_directory_path),
        ),
    ]