FROM python:3.10.4

ARG COMPONENT_PATH

RUN mkdir /usr/src/app
WORKDIR /usr/src/app

COPY ./$COMPONENT_PATH/requirements.txt .
RUN pip3 install -r requirements.txt

ENV PYTHONUNBUFFERED 1

COPY ./${COMPONENT_PATH} .


CMD ["python3", "main.py"]