from sqlalchemy import create_engine
    
import networkx
from networkx.algorithms.components.connected import connected_components

import pandas as pd
import numpy as np
import os
import boto3

import tensorflow as tf
import tensorflow_hub as hub

module_url = "https://tfhub.dev/google/universal-sentence-encoder-large/3"
embed = hub.Module(module_url)

user=os.getenv('user') or 'root'
passwd=os.getenv('passwd')
server=os.getenv('server')
port=os.getenv('port') or '5439'
dbname=os.getenv('dbname') or 'vdb'
senderid=os.getenv('senderid')
access=os.getenv('access')
secret=os.getenv('secret')
bucket=os.getenv('bucket') or 'athenadata162'
mylimit=os.getenv('mylimit') or '0.8'

pg_engine = create_engine(
    "postgresql+psycopg2://%s:%s@%s:%i/%s" % (user, passwd, server, int(port), dbname)
)

def uniqueGroup(groups):
    def to_graph(groups):
        G = networkx.Graph()
        for part in groups:
            G.add_nodes_from(part)
            G.add_edges_from(to_edges(part))
        return G

    def to_edges(groups):
        it = iter(groups)
        last = next(it)

        for current in it:
            yield last, current
            last = current

    G = to_graph(groups)
    return connected_components(G)
        
def clusterize(mysenderid):
    my_query = (
        "select * from temple_senderid_merge_u3 where senderid = '" + mysenderid + "' limit 1000000 "
    )
    df = pd.read_sql(my_query, con=pg_engine)
    df = df.dropna()

    messages = df.new_message.values.ravel()

    ml_df_collect = list()

    similarity_input_placeholder = tf.placeholder(tf.string, shape=(None))
    similarity_message_encodings = embed(similarity_input_placeholder)
    with tf.Session() as session:
        session.run(tf.global_variables_initializer())
        session.run(tf.tables_initializer())
        message_embeddings_ = session.run(
            similarity_message_encodings,
            feed_dict={similarity_input_placeholder: messages},
        )
    corr = np.inner(message_embeddings_, message_embeddings_)
    ml_df_collect.append(corr)

    ndf = pd.DataFrame(ml_df_collect[0])
    np.fill_diagonal(ndf.values, 0)
    ndf = pd.DataFrame(ndf.values)
    tups = list(ndf[ndf > float(mylimit)].stack().index)
        

    x = uniqueGroup(tups)
    mylist = list()
    for i, x in enumerate(x):
        for id in x:
            mylist.append((id, i))

    sdf = pd.DataFrame(mylist)
    sdf.columns = ["message_id", "cluster_id"]
    sdf = sdf.set_index("message_id")
    final = df.join(sdf)
    return final
    
    
clusterize(senderid).to_csv(senderid+'.csv')

session = boto3.Session(aws_access_key_id= access, aws_secret_access_key=secret)
s3 = session.resource('s3')
s3.meta.client.upload_file(Filename=senderid + ".csv", Bucket=bucket, Key=senderid + ".csv")
