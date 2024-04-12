FROM python:3.12
 
WORKDIR /app

ADD . ./
 
RUN pip install --no-cache-dir -r requirements.txt