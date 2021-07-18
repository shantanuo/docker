FROM ubuntu
RUN apt update && apt --yes install libxml-xpath-perl wget unzip curl

RUN curl "https://awscli.amazonaws.com/awscli-exe-linux-x86_64.zip" -o "awscliv2.zip"
RUN unzip awscliv2.zip
RUN ./aws/install

ADD update_feed.sh /tmp/

aws s3 ls
