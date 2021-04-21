FROM ubuntu:20.04

RUN apt-get update -y && \
    apt-get install -y python3-pip python3-dev

# We copy just the requirements.txt first to leverage Docker cache
COPY ./requirements.txt /app/requirements.txt

WORKDIR /app

RUN pip3 install -r requirements.txt

COPY . /app

EXPOSE 3500

#ENTRYPOINT [ "python3" ]

CMD ["python3","server.py"]
#CMD [ "nohup","python3","server.py", "&" ]
