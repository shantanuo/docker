FROM continuumio/miniconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet
EXPOSE 8888
RUN cd /tmp/
RUN apt-get update
RUN apt-get install --yes python-pydot build-essential
RUN conda install --yes -c conda-forge fastparquet pydotplus
RUN pip install -U numpy seaborn sklearn spacy pillow bs4 nb_black pyjanitor psycopg2-binary sqlalchemy  boto3
COPY nlp_kmeans.py /tmp/nlp_kmeans.py
