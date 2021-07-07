from django.db import models


class Rate(models.Model):

    RATE_TYPE_USD = 10
    RATE_TYPE_EUR = 11

    RATE_TYPE_CHOICES = (
        (RATE_TYPE_USD, 'Dollar'),
        (RATE_TYPE_EUR, 'Euro'),
    )

    cur_type = models.PositiveSmallIntegerField(choices=RATE_TYPE_CHOICES)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=128)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=999)
    created = models.DateTimeField(auto_now_add=True)


class Source(models.Model):
    name = models.CharField(max_length=12)
    url = models.URLField(max_length=255)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
