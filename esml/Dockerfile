FROM openjdk:jre-alpine
ARG ek_version=6.2.1

RUN apk add --quiet --no-progress --no-cache nodejs wget git curl\
 && adduser -D elasticsearch

RUN apk add --no-cache python3 \
&& python3 -m ensurepip \
&& pip3 install --upgrade pip setuptools \
&& rm -r /usr/lib/python*/ensurepip && \
if [ ! -e /usr/bin/pip ]; then ln -s pip3 /usr/bin/pip ; fi && \
if [[ ! -e /usr/bin/python ]]; then ln -sf /usr/bin/python3 /usr/bin/python; fi && \
rm -r /root/.cache

WORKDIR /home/elasticsearch
RUN pip install requests  elasticsearch==5.5.3
RUN git clone  https://github.com/o19s/elasticsearch-learning-to-rank.git
RUN chmod -R 777 /home/elasticsearch/elasticsearch-learning-to-rank

USER elasticsearch

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

RUN sh /home/elasticsearch/elasticsearch/bin/elasticsearch-plugin install -b http://es-learn-to-rank.labs.o19s.com/ltr-1.0.1-es6.2.1.zip

CMD sh elasticsearch/bin/elasticsearch -E http.host=0.0.0.0 --quiet & kibana/bin/kibana --host 0.0.0.0 -Q

EXPOSE 9200 5601
