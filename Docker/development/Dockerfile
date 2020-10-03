FROM python:3.7.6


ENV PYTHONPATH=/app/source

COPY . /app
WORKDIR /app

RUN pip install --upgrade pip
RUN pip install -r Docker/development/requirements.txt
EXPOSE 8000
