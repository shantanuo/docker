FROM python:2
RUN git clone https://github.com/CognirelTech/Quillpad-Server.git
RUN cd Quillpad-Server/Python\ Cart/python/ && python setup.py build_ext --inplace
RUN cp Quillpad-Server/Python\ Cart/python/QuillCCart.so .
CMD [ "python", "./startquill_cherry.py" ]
