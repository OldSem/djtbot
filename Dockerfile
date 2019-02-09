FROM python:3.6

ENV PYTHONUNBUFFERED 1
ENV C_FORCE_ROOT true

RUN mkdir /djtbot
RUN mkdir /static

WORKDIR /djtbot
ADD ./djtbot /djtbot
RUN pip install --upgrade pip
RUN pip install -r requirements.txt
CMD python manage.py collectstatic --no-input;python manage.py migrate; gunicorn djtbot.wsgi -b 0.0.0.0:8000
#& celery worker --app=myapp.tasks