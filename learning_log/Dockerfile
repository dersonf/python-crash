FROM python:3.8-alpine

ENV DEBUG FALSE

WORKDIR /usr/src/app

COPY . .

RUN pip install --no-cache-dir -r requirements.txt && \
    apk add tzdata && \
    cp /usr/share/zoneinfo/America/Sao_Paulo /etc/localtime

EXPOSE 8000/tcp

ENTRYPOINT python manage.py runserver 0.0.0.0:8000
