FROM python:3
ENV PYTHONUNBUFFERED 1
RUN mkdir /keygen
RUN mkdir /var/log/celery
WORKDIR /keygen
COPY ./requirements.txt /keygen/
RUN pip install --upgrade pip && pip install -r requirements.txt
COPY . /keygen/
COPY ./entrypoint.sh /keygen/