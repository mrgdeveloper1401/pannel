FROM python:3.12-alpine

WORKDIR /home/app

COPY . .

RUN apk update --no-cache && \
    apk upgrade --no-cache && \
    apk add py3-pip && \
    pip install --upgrade pip && \
    pip install -r ./requirements/production.txt && \
    adduser -D -H panel && \
    chown -R panel:panel /home/app && \
    chmod +x ./start.sh && \
    chmod +x ./manage.py && \
    mkdir media


ENV PYTHONDONOTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

EXPOSE 8000

USER panel

ENTRYPOINT ["sh", "-c", "/home/app/start.sh"]
