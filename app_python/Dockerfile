# syntax=docker/dockerfile:1
FROM python:3.8-alpine

WORKDIR /home/app_python
ENV FLASK_APP=main.py

RUN apk add --no-cache gcc \
  musl-dev \
  linux-headers

COPY requirements.txt requirements.txt
RUN pip install --no-cache -r requirements.txt

COPY . .
EXPOSE 5000

CMD ["python3", "-m", "flask", "run", "--host=0.0.0.0"]