FROM continuumio/miniconda3
RUN /opt/conda/bin/conda install jupyter -y --quiet
EXPOSE 8888
RUN cd /tmp/
RUN apt-get update
RUN apt-get install --yes python-pydot build-essential zip
RUN conda install --yes -c conda-forge fastparquet pydotplus
RUN pip install -U numpy seaborn sklearn spacy pillow bs4 nb_black pyjanitor psycopg2-binary sqlalchemy  boto3
RUN pip install -U nltk boto spello symspellpy
RUN wget https://raw.githubusercontent.com/hitz02/Sentiment_Analysis_Phone_Review/master/K8%20Reviews%20v0.2.csv
RUN wget https://www.dropbox.com/s/v9uuv635lv1idjf/en_large.pkl.zip
RUN unzip en_large.pkl.zip
RUN cp en_large.pkl /tmp/en_large.pkl

RUN cp K8\ Reviews\ v0.2.csv /tmp/K8\ Reviews\ v0.2.csv
COPY df_process.py /tmp/df_process.py
