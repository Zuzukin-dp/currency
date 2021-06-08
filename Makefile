SHELL := /bin/bash

manage_p := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate
