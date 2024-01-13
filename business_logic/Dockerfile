FROM python:3.8

ADD . /api
WORKDIR /api

RUN pip3 install -r requirements.txt

CMD python backend_server.py