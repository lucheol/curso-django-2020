FROM python:3.7-slim
ENV PYTHONUNBUFFERED 1
RUN apt-get update -y

RUN apt-get -y install binutils libproj-dev gdal-bin
RUN apt-get -y install libjpeg-dev
RUN apt-get -y install zlib1g-dev
RUN apt-get -y install nano curl

RUN mkdir /code
WORKDIR /code
ADD requirements.txt /code/
RUN pip install --upgrade pip
RUN pip install -r requirements.txt