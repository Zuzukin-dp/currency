# currency

[Link to clone the repository](https://github.com/Zuzukin-dp/currency.git)

[Git for half an hour](https://proglib.io/p/git-for-half-an-hour)

#### create a virtual environment
'$ python3 -m venv env'
#### activate a virtual environment
'$ . env/bin/activate'

'$ pip install -r requirements.txt'

[sqlite3 basics](https://docs.python.org/3/library/sqlite3.html), 
[DjangoGirls Tutorial](https://tutorial.djangogirls.org/ru/), 
[Flask VS Django](https://django.fun/tutorials/flask-vs-django-sravnenie-sozdaniya-rest-api/),
[QuerySet API reference](https://docs.djangoproject.com/en/3.1/ref/models/querysets/),
[Django ORM](https://books.agiliq.com/projects/django-orm-cookbook/en/latest/),
[Django templates](https://tutorial.djangogirls.org/ru/django_templates/),
[HTTP status code](https://ru.wikipedia.org/wiki/%D0%A1%D0%BF%D0%B8%D1%81%D0%BE%D0%BA_%D0%BA%D0%BE%D0%B4%D0%BE%D0%B2_%D1%81%D0%BE%D1%81%D1%82%D0%BE%D1%8F%D0%BD%D0%B8%D1%8F_HTTP)

'$ python ./add/manage.py migrate'

'$ python ./add/manage.py runserver'

# for ipython, run console + import django packages 
'$ python ./add/manage.py shell_plus --print-sql'

'$ python manage.py shell_plus --print-sql'

# For Celery

'$ sudo service rabbitmq-server start'

'$ sudo service rabbitmq-server status'

'$ celery -A settings worker -l info'
