FROM continuumio/miniconda3
EXPOSE 8888
RUN cd /tmp/
RUN pip install -U numpy seaborn sklearn spacy pillow bs4 nb_black pyjanitor psycopg2-binary sqlalchemy boto3
COPY nlp_kmeans.py /tmp/nlp_kmeans.py
