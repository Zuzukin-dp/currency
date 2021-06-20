from celery import shared_task

from django.core.mail import send_mail


@shared_task
def print_hallo(object_id):
    from currency.models import ContactUs
    ContactUs.objects.get(id=object_id)
    print(f'ContactUs id: {object_id}')


@shared_task(
    autoretry_for=(Exception,),
    retry_kwargs={
        'max_retries': 5,
        'default_retry_delay': 30},
)
def task_send_email(body):
    send_mail(
        'Contact Us from Client',
        body,
        'pydjantest@gmail.com',
        ['pydjantest@gmail.com'],
        fail_silently=False,
    )