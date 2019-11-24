FROM openjdk:jre-alpine

LABEL maintainer "nshou <nshou@coronocoya.net>"

ARG ek_version=6.2.1

RUN apk add --quiet --no-progress --no-cache nodejs wget curl\
 && adduser -D elasticsearch

RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

USER elasticsearch

WORKDIR /home/elasticsearch

ENV ES_TMPDIR=/home/elasticsearch/elasticsearch.tmp

RUN wget -q -O - https://artifacts.elastic.co/downloads/elasticsearch/elasticsearch-${ek_version}.tar.gz \
 |  tar -zx \
 && mv elasticsearch-${ek_version} elasticsearch \
 && mkdir -p ${ES_TMPDIR} \
 && wget -q -O - https://artifacts.elastic.co/downloads/kibana/kibana-${ek_version}-linux-x86_64.tar.gz \
 |  tar -zx \
 && mv kibana-${ek_version}-linux-x86_64 kibana \
 && rm -f kibana/node/bin/node kibana/node/bin/npm \
 && ln -s $(which node) kibana/node/bin/node \
 && ln -s $(which npm) kibana/node/bin/npm

CMD sh elasticsearch/bin/elasticsearch -E http.host=0.0.0.0 --quiet & kibana/bin/kibana --host 0.0.0.0 -Q

EXPOSE 9200 5601
