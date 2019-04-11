FROM python:3.5
ARG BUILD_VERSION=0.0.1.1

ENV LANG=C.UTF-8

COPY . /work
WORKDIR /work

RUN pip install -r requirements.txt -i https://pypi.douban.com/simple
RUN echo "VERSION='${BUILD_VERSION}'" > /work/django_celery_schedule/__init__.py

EXPOSE 13777


CMD ["python","manage.py","runserver","0.0.0.0:13777"]
