FROM continuumio/miniconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet
EXPOSE 8888
RUN cd /tmp/
RUN apt-get update
RUN apt-get install --yes python-pydot build-essential
RUN conda install --yes -c conda-forge fastparquet pydotplus
RUN pip install -U seaborn sklearn pillow bs4 nb_black pyjanitor psycopg2-binary sqlalchemy boto3 networkx tensorflow tensorflow_hub
COPY nlp_tensorflow.py /tmp/nlp_tensorflow.py
