FROM python:3.7.6

RUN apt update
RUN apt -y install postgresql-client-11 postgresql-client-common

ENV PYTHONPATH=/app/source

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r Docker/development/requirements.txt
EXPOSE 8000
