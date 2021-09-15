SHELL := /bin/bash

#manage_py := python ./app/manage.py
manage_py := docker exec -it backend python ./app/manage.py

#build:
#	docker-compose down && docker-compose up -d

build:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml up -d --build

down:
	docker-compose -f docker-compose.yml -f docker-compose.dev.yml down

runserver:
	$(manage_py) runserver 0:8001

collectstatic:
	$(manage_py) collectstatic --noinput && \
	docker cp backend:/tmp/static /tmp/static && \
	docker cp /tmp/static nginx:/etc/nginx/static

gunicorn:
	cd app/ && gunicorn -w 4 settings.wsgi:application -b 0.0.0.0:8000 --log-level=DEBUG

gunicorn01:
	cd app/ && gunicorn -w 4 settings.wsgi:application -b 127.0.0.1:8001 --log-level=DEBUG

uwsgi:
	cd app/ && uwsgi --http :8000 --module settings.wsgi --master --processes 4

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
	pytest app/tests/ --cov=app --cov-report html  && coverage report --fail-under=60.6

show-coverage:  ## open coverage HTML report in default browser
	python3 -c "import webbrowser; webbrowser.open('.pytest_cache/coverage/index.html')"

#collectstatic:
	#$(manage_py) collectstatic --noinput
