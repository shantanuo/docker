FROM python:2
RUN pip install cherrypy mysqlclient
RUN git clone https://github.com/CognirelTech/Quillpad-Server.git
WORKDIR Quillpad-Server/
RUN mkdir logs

RUN cd Python\ Cart/python/ && python setup.py build_ext --inplace
RUN cp Python\ Cart/python/QuillCCart.so .

RUN wget http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-0.9.9.tar.gz
RUN tar xf Pyrex-0.9.9.tar.gz
RUN ls *.tar.bz2 | xargs -i tar xf {}
RUN unzip \*.zip
RUN cd Pyrex-0.9.9 && python setup.py install

CMD [ "python", "./startquill_cherry.py" ]
