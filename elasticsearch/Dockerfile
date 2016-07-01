FROM ubuntu:latest
MAINTAINER  <shantanu.oak@gmail.com>
RUN apt-get update -q
RUN apt-get install -yq wget default-jre-headless curl parallel
RUN useradd -m elasticsearch
USER elasticsearch
WORKDIR /home/elasticsearch
ENV ES_VERSION 2.1.1

RUN wget -nv https://download.elasticsearch.org/elasticsearch/release/org/elasticsearch/distribution/tar/elasticsearch/${ES_VERSION}/elasticsearch-${ES_VERSION}.tar.gz && \
    tar zxf elasticsearch-${ES_VERSION}.tar.gz && \
    rm -f elasticsearch-${ES_VERSION}.tar.gz && \
    mv elasticsearch-${ES_VERSION} elasticsearch

ENV KIBANA_VERSION 4.3.1

RUN wget -nv https://download.elastic.co/kibana/kibana/kibana-${KIBANA_VERSION}-linux-x64.tar.gz && \
    tar zxf kibana-${KIBANA_VERSION}-linux-x64.tar.gz && \
    rm -f kibana-${KIBANA_VERSION}-linux-x64.tar.gz && \
    mv kibana-${KIBANA_VERSION}-linux-x64 kibana
    
# RUN wget https://dumps.wikimedia.org/other/cirrussearch/20160502/emlwiki-20160502-cirrussearch-content.json.gz

# RUN gunzip emlwiki-20160502-cirrussearch-content.json.gz

CMD elasticsearch/bin/elasticsearch -Des.logger.level=OFF -Des.network.bind_host=0.0.0.0 & kibana/bin/kibana -q

EXPOSE 9200 5601
