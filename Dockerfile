FROM python:3
ADD . /istari
WORKDIR /istari
RUN pip3 install -r requirements.txt
