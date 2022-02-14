FROM python:2
RUN git clone https://github.com/CognirelTech/Quillpad-Server.git
RUN cd Quillpad-Server/Python\ Cart/python/ && python setup.py build_ext --inplace
RUN cp Quillpad-Server/Python\ Cart/python/QuillCCart.so .

RUN pip install cherrypy mysqlclient
RUN wget http://www.cosc.canterbury.ac.nz/greg.ewing/python/Pyrex/Pyrex-0.9.9.tar.gz

RUN tar -xvf marathi.tar.bz2
RUN tar -xvf nepali.tar.bz2
RUN tar -xvf punjabi.tar.bz2
RUN tar -xvf tamil.tar.bz2
RUN tar -xvf telugu.tar.bz2
RUN tar -xvf EnglishPronouncingTrees.tar.bz2
RUN tar -xvf IndianPronouncingTrees.tar.bz2
RUN tar -xvf bengali.tar.bz2
RUN tar -xvf gujarati.tar.bz2
RUN tar -xvf hindi.tar.bz2
RUN tar -xvf kannada.tar.bz2
RUN tar -xvf malayalam.tar.bz2
RUN tar -xvf Pyrex-0.9.9.tar.gz

RUN unzip \*.zip
RUN cd Pyrex-0.9.9 && python setup.py install

CMD [ "python", "./startquill_cherry.py" ]
