FROM alpine
RUN \
  apk update && \
  apk upgrade && \
  apk add perl wget zip && \
  apk add --virtual .build curl make

RUN wget --no-check-certificate -O master.zip https://github.com/darold/pgbadger/archive/master.zip

RUN unzip master.zip

ADD . /workdir
RUN \
  ( \
    cd /workdir/pgbadger-master && \
    perl Makefile.PL && \
    make install \
  ) && \
  apk del --purge .build && \
  rm -rf /workdir/

WORKDIR /workdir
ENTRYPOINT ["/usr/local/bin/pgbadger"]
CMD ["--help"]
