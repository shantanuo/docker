Dockerfile is like this...

FROM alpine
RUN apk add --update python && rm -rf /var/cache/apk/*

ADD client2.py /

client2.py is python scoket client 

Use this container as shown below:

docker run -it shantanuo/socket /bin/sh

python client2.py

