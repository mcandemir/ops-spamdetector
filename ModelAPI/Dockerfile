# syntax=docker/dockerfile:1
FROM tensorflow/tensorflow:latest

WORKDIR /ModelAPI-docker

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

COPY . .

CMD ["python3", "app.py"]