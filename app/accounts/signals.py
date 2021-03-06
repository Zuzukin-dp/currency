from accounts.models import User

from django.db.models.signals import pre_save
from django.dispatch import receiver


@receiver(pre_save, sender=User)
def pre_save_user(sender, instance, **kwargs):
    if instance.email:
        instance.email = instance.email.lower()

    # instance.phone = ''.join(char for char in instance.phone if char.isdigit())
    # print('PRE SAVE SIGNALS')


# @receiver(post_save, sender=User)
# def post_save_user(sender, instance, created, **kwargs):
#     # print(f'Instance is created: {created} instance: {instance}')
#     # instance.save()
#     if created:
#         request.post()
#         print('POST SAVE SIGNALS')
#     pass


# class DeleteIsNotAllowed(Exception):
#     pass
#
#
# @receiver(pre_delete, sender=User)
# def stop_delete(*args, **kwargs):
#     raise DeleteIsNotAllowed('Instance could not be deleted')
