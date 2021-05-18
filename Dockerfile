FROM python:3.7-slim-buster

WORKDIR /app

ENV VIRTUAL_ENV=/opt/venv
RUN python3 -m venv $VIRTUAL_ENV
ENV PATH="$VIRTUAL_ENV/bin:$PATH"

# Download latest listing of available packages:
RUN apt-get -y update
## Upgrade already installed packages:
RUN apt-get -y upgrade
## Install a new package:
RUN apt-get -y install python3-gi gstreamer-1.0

RUN ln -s /usr/lib/python3/dist-packages/gi /opt/venv/lib/python3.7/site-packages/

COPY requirements.txt requirements.txt
RUN . /opt/venv/bin/activate && pip install -r requirements.txt


COPY src src

CMD . /opt/venv/bin/activate && exec python3 src/main.py


