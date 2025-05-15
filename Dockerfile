FROM python:3.11-slim

WORKDIR /app

COPY gigazine/ ./gigazine/
COPY requirements.txt ./

RUN pip install --upgrade pip && \
    pip install -r requirements.txt

WORKDIR /app/gigazine
