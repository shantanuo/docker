import pandas as pd
from datetime import datetime
import boto3
import fire
import os

MY_ACCESS_KEY_ID = os.environ.get('MY_ACCESS_KEY_ID') 
MY_SECRET_ACCESS_KEY = os.environ.get('MY_SECRET_ACCESS_KEY')

s3_client = boto3.client('s3', aws_access_key_id= MY_ACCESS_KEY_ID, aws_secret_access_key= MY_SECRET_ACCESS_KEY)

mystring='updated_'

def convertdate(filename):
    df=pd.read_csv(filename) 
    df['message']=df.message.replace('\n', '', regex=True)
    try:
        for i in ['sent_date', 'event_datetime', 'done_date', 'insert_date' ]:
            df[i]=df[i].apply(lambda x: datetime.fromtimestamp(float(x)/1000))
            pd.to_timedelta(df[i], errors = 'coerce')
    except:
        pass
    df.to_csv(mystring+filename, sep='\t', encoding='utf-8')
    s3_client.upload_file(mystring+filename, '13cols', 'csv1/'+mystring+filename)

if __name__ == '__main__':
    try:
        fire.Fire(convertdate)
    except:
        print ("error found", filename)
