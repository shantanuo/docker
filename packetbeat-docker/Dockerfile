FROM docker.elastic.co/beats/packetbeat:6.2.2
COPY packetbeat.yml /usr/share/packetbeat/packetbeat.yml
COPY packetbeat.template-es6x.json /usr/share/packetbeat/packetbeat.template-es6x.json
USER root
RUN chown packetbeat /usr/share/packetbeat/packetbeat.yml
RUN chown packetbeat /usr/share/packetbeat/packetbeat.template-es6x.json
USER packetbeat
