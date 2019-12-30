FROM python
ADD https://sourceforge.net/projects/hunspell/files/Hyphen/2.8/hyphen-2.8.8.tar.gz/download hyphen
RUN tar -xvf hyphen
ADD myinstall.sh /myinstall.sh
ADD hi_sample.text /tmp/hi_sample.text
RUN sh /myinstall.sh
RUN wget https://extensions.libreoffice.org/extensions/marathi-spellchecker/1.8/@@download/file/with_hyphen.oxt
RUN apt-get install unzip
RUN unzip with_hyphen.oxt
WORKDIR /hyphen-2.8.8
