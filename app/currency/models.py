from currency import choices

from django.db import models


class Source(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)
    url = models.URLField(max_length=255)
    original_url = models.URLField(max_length=255)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)


class Rate(models.Model):
    cur_type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    bank = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
    )


class ContactUs(models.Model):
    email_from = models.EmailField(max_length=128)
    subject = models.CharField(max_length=255)
    message = models.CharField(max_length=999)
    created = models.DateTimeField(auto_now_add=True)


class Analytics(models.Model):
    path = models.CharField(max_length=255)
    counter = models.PositiveBigIntegerField()
    request_method = models.PositiveSmallIntegerField(choices=choices.REQUEST_METHOD_CHOICES)
    status = models.PositiveSmallIntegerField()

    class Meta:
        unique_together = [
            ['path', 'request_method', 'status'],
        ]
