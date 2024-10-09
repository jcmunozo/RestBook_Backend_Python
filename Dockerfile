FROM python:3

ENV PYTHONUNBUFFERED 1
RUN mkdir /restbook_api
WORKDIR /restbook_api
COPY . /restbook_api/
RUN pip install -r requirements.txt
