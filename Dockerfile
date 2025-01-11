FROM python:3.11-alpine3.16

WORKDIR /dogs_django

COPY requirements.txt /dogs_django/requirements.txt
RUN pip install -r /dogs_django/requirements.txt

COPY dogs_django /dogs_django

RUN adduser --disabled-password --home /dogs_django s4bject \
    && chown -R s4bject:s4bject /dogs_django

USER s4bject

EXPOSE 8000
