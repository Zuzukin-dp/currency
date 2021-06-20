SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

makemigrations:
	$(manage_py) makemigrations

migrate:
	$(manage_py) migrate

show_urls:
	$(manage_py) show_urls

shell:
	$(manage_py) shell_plus --print-sql

freeze:
	pip freeze > requirements.txt

createsuperuser:
	$(manage_py) createsuperuser

worker10:
	cd app && celery -A settings worker -l info -c 10

worker:
	cd app && celery -A settings worker -l info --autoscale=0,20