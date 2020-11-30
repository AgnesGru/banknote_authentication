
FROM ubuntu:20.04

RUN apt update -y && \
apt install -y python3-pip python3-dev

COPY . /usr/app/

EXPOSE 5000

WORKDIR /usr/app/

RUN pip3 install -r requirements.txt

ENTRYPOINT ["python3"]

CMD [ "app.py" ]
