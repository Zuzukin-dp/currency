FROM python:3.9

WORKDIR /home/prod

COPY requirements.txt .

# RUN apt update -y && apt install -y curl

RUN pip install -r requirements.txt

# for pathon module and packeges
ENV PYTHONPATH "/home/prod/app"

COPY . .

CMD ["gunicorn", "-w", "4", "-b", "0.0.0.0:8000", "--chdir", "/home/prod/app", "settings.wsgi", "--timeout 30", "--log-level error", "--max-requests 10000"]

#CMD ["python", "app/manage.py", "runserver", "0.0.0.0:8000"]
