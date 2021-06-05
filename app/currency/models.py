from django.db import models


class Rate(models.Model):
    cur_type = models.CharField(max_length=5)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    source = models.CharField(max_length=64)


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=128)
    subject = models.CharField(max_length=12)
    message = models.TextField()


class Source(models.Model):
    name = models.CharField(max_length=12)
    url = models.URLField(max_length=255)
    phone = models.CharField(max_length=13)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
