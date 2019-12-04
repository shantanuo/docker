#!/usr/bin/env python
# coding: utf-8

#!pip install psycopg2-binary sqlalchemy pandas boto3

from sqlalchemy import create_engine

import pandas as pd
import numpy as np
import os
import boto3

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.feature_extraction.text import CountVectorizer
from sklearn.cluster import KMeans

user = os.environ["user"] or "root"
passwd = os.environ["passwd"]
server = os.environ["server"]
port = os.environ["port"] or "5439"
dbname = os.environ["dbname"] or "vdb"
senderid = os.environ["senderid"]
access = os.environ["access"] 
secret = os.environ["secret"]

pg_engine = create_engine(
    "postgresql+psycopg2://%s:%s@%s:%i/%s" % (user, passwd, server, int(port), dbname)
)

my_query = (
    "select new_message from temple_senderid_merge_u3 where senderid = '"
    + senderid
    + "' limit 1000000 "
)
df = pd.read_sql(my_query, con=pg_engine)
df = df.dropna()

myreplace = {"\,": "[variable]", "\:": "[variable]", "\.": "[variable]"}
pdf1 = df.replace(myreplace, regex=True)

try:
    sdf = pdf1.new_message.str.split(n=1, expand=True)
    sdf.columns = ["first", "rest"]
    s = sdf.groupby("first").count()
    elbow = s[s > s.quantile(0.95)].dropna().count()
    if elbow["rest"] == 0:
        nelbow = 1
    else:
        nelbow = elbow["rest"]
except:
    nelbow = 1

messages = df.values.ravel()
messages1 = messages[messages != np.array(None)]
tf = TfidfVectorizer()
tfidf_matrix = tf.fit_transform(messages1)
ndf = pd.SparseDataFrame(tfidf_matrix)
ndf.columns = tf.get_feature_names()
X = ndf.fillna("0")

kmeans = KMeans(n_clusters=nelbow)
pred = kmeans.fit_predict(X)

ml_df = pd.DataFrame()
ml_df["messages"] = messages
ml_df["template_types"] = pred
ml_df["senderid"] = senderid
ml_df.to_csv(senderid + ".csv")

session = boto3.Session(
    aws_access_key_id= access,
    aws_secret_access_key=secret
)
s3 = session.resource('s3')
s3.meta.client.upload_file(Filename=senderid + ".csv", Bucket='athenadata162', Key=senderid + ".csv")
