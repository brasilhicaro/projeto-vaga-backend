# Imagem com erro
FROM python:3.12
RUN python -m pip install --upgrade pip
RUN apt-get update && apt-get install -y libpq-dev build-essential
WORKDIR /app

COPY requirements.txt .

RUN pip install -r requirements.txt

COPY . .

EXPOSE 8000

