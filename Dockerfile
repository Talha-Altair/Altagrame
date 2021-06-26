FROM python:3.9.5-slim-buster

ADD . /altair

WORKDIR /altair

RUN pip install -r "requirements.txt"

CMD [ "python":"app.py" ]
