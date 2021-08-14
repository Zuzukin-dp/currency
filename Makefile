SHELL := /bin/bash

manage_py := python ./app/manage.py

runserver:
	$(manage_py) runserver 127.0.0.1:8000

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

worker:
	cd app && celery -A settings worker -l info

worker20:
	cd app && celery -A settings worker -l info --autoscale=0,20

beat:
	cd app && celery -A settings beat -l info

pytest:
	pytest app/tests/ -s -vvv

pytest_cov:
	pytest app/tests/ --cov=app --cov-report html ## && coverage report --fail-under=80

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"
