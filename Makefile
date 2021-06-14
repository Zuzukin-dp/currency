SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 0:8000

migrate:
	$(manage_py) migrate

show_urls:
	$(manage_py) show_urls

shell:
	$(manage_py) shell_plus --print-sql
