FROM python:2
RUN git clone https://github.com/CognirelTech/Quillpad-Server.git
RUN cd Quillpad-Server/Python\ Cart/python/ && python setup.py build_ext --inplace
RUN cp Quillpad-Server/Python\ Cart/python/QuillCCart.so .

RUN pip install cherrypy mysqlclient
RUN for f in *.tar.bz2; do tar -xvf "$f"; done
RUN unzip \*.zip

CMD [ "python", "./startquill_cherry.py" ]
