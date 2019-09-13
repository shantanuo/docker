import pandas as pd
import numpy as np
import os
import awswrangler

ENVIRON_ACCESS_KEY = os.environ['AWS_ACCESS_KEY_ID']
ENVIRON_SECRET_KEY = os.environ['AWS_SECRET_ACCESS_KEY']
ENVIRON_S3_PATH = os.environ['s3_path']
ENVIRON_CSV_PATH = os.environ['csv_path']

df = pd.read_csv(ENVIRON_CSV_PATH)
df = df.astype(str)

session = awswrangler.Session(aws_access_key_id=ENVIRON_ACCESS_KEY, aws_secret_access_key=ENVIRON_SECRET_KEY)
session.pandas.to_parquet(dataframe=df, path=ENVIRON_S3_PATH)
