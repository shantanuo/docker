FROM alpine
RUN \
  apk update && \
  apk upgrade && \
  apk add perl git && \
  apk add --virtual .build curl make

RUN git clone https://github.com/darold/pgbadger.git

ADD . /workdir
RUN \
  ( \
    cd /workdir/pgbadger && \
    perl Makefile.PL && \
    make install \
  ) && \
  apk del --purge .build && \
  rm -rf /workdir/*

WORKDIR /workdir
ENTRYPOINT ["/usr/local/bin/pgbadger"]
CMD ["--help"]
