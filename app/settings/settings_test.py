from settings.settings import *

CELERY_TASK_ALWAYS_EAGER = True

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only

DEBUG = False
