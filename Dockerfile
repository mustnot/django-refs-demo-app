FROM python:3.10-bullseye

ENV PYTHONDONTWRITEBYTECODE=1
ENV PYTHONUNBUFFERED=1

WORKDIR /web

RUN pip install --upgrade pip setuptools wheel

COPY requirements.txt .
RUN pip install -r requirements.txt

COPY . .
RUN chmod 755 ./docker-entrypoint.sh


EXPOSE 8000

ENTRYPOINT ["./docker-entrypoint.sh"]
