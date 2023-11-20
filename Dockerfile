FROM python:3.8


COPY requirements.txt .

RUN pip install -r requirements.txt

COPY ./src ./src
COPY ./model.pkl ./model.pkl
COPY ./encoder.pkl ./encoder.pkl