FROM python:3.11 as base
ENV PYTHONUNBUFFERED 1
ENV ENVIRONMENT=dev

WORKDIR /app

COPY ./django .
RUN pip3 install -r requirements.txt