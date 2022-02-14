FROM python:2
RUN git clone https://github.com/CognirelTech/Quillpad-Server.git
RUN cd Quillpad-Server/Python\ Cart/python/ && python setup.py build_ext --inplace
RUN cp Quillpad-Server/Python\ Cart/python/QuillCCart.so .

RUN pip install cherrypy mysqlclient
RUN wget http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-0.9.9.tar.gz

RUN for f in *.tar.bz2; do tar -xvf "$f"; done
RUN unzip \*.zip
RUN cd Pyrex-0.9.9 && python setup.py install

CMD [ "python", "./startquill_cherry.py" ]
