FROM python
RUN apt-get update && apt-get install --yes unzip vim
ADD https://sourceforge.net/projects/hunspell/files/Hyphen/2.8/hyphen-2.8.8.tar.gz/download hyphen
RUN tar -xvf hyphen
ADD myinstall.sh /myinstall.sh
RUN sh /myinstall.sh
RUN wget https://extensions.libreoffice.org/extensions/marathi-spellchecker/1.8/@@download/file/with_hyphen.oxt
RUN unzip with_hyphen.oxt
ADD hi_sample.text /hi_sample.text
WORKDIR /hyphen-2.8.8
