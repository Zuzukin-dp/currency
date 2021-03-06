from currency import choices

from django.db import models
from django.templatetags.static import static


def source_directory_path(instance, filename):
    return 'uploads/source_logo/{0}/{1}'.format(instance.id, filename)


class Source(models.Model):
    name = models.CharField(max_length=64)
    code_name = models.CharField(max_length=64, unique=True)
    url = models.URLField(max_length=255)
    original_url = models.URLField(max_length=255)
    phone = models.CharField(max_length=20)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    source_logo = models.FileField(null=True, blank=True, default=None, upload_to=source_directory_path)

    def get_source_logo_url(self):
        if self.source_logo:
            return self.source_logo.url
        return static('img/default-source-logo.jpg')

    def __str__(self):
        return f'{self.name}'


class Rate(models.Model):
    cur_type = models.PositiveSmallIntegerField(choices=choices.RATE_TYPE_CHOICES)
    sale = models.DecimalField(max_digits=5, decimal_places=2)
    buy = models.DecimalField(max_digits=5, decimal_places=2)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    bank = models.ForeignKey(
        Source,
        on_delete=models.CASCADE,
    )

    def __str__(self):
        return f'Rate id: {self.id} {self.bank_id}'


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
