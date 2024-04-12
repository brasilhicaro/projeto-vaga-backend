FROM python:3.12
 
WORKDIR /app

ADD . ./

RUN apt-get update && apt-get install -y libpq-dev build-essential

RUN pip install --no-cache-dir -r requirements.txt