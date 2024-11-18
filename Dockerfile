FROM ubuntu:latest
LABEL authors="Administrator"
FROM python:3.11.9-slim

WORKDIR /app

COPY . .

RUN pip install -r requirements.txt

EXPOSE 5000

ENTRYPOINT ["python", "app.py"]