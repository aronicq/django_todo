FROM python:3.8

RUN pip install gunicorn django djangorestframework djangorestframework-simplejwt

COPY ./ code/
WORKDIR /code

RUN ls
# RUN gunicorn django_project.wsgi --bind 0.0.0.0:8000

EXPOSE 8000