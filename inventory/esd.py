import requests
from io import StringIO
import pandas as pd
import numpy as np
import boto3
import os

my_url=os.environ.get('my_url')
my_post_url=os.environ.get('my_post_url') 
my_user=os.environ.get('my_user')  
my_password=os.environ.get('my_password') 
MY_ACCESS_KEY_ID = os.environ.get('MY_ACCESS_KEY_ID') 
MY_SECRET_ACCESS_KEY = os.environ.get('MY_SECRET_ACCESS_KEY')


url = my_url
values = {'txt_user_name': my_user,
         'txt_password': my_password}

s = requests.Session() 
s.post(url, data=values)

r2 = requests.post(my_post_url,cookies=s.cookies)
print (r2.content.decode("utf-8"))
df = pd.read_csv(StringIO(r2.content.decode("utf-8")) )

df.columns=['Sr_No', 'Device_Name', 'Device_Ip', 'Memory_min', 'Memory', 'memory_avg', 'memory_total', 'Unnamed1', 'CPU_min', 'CPU', 'CPU_avg', 'Unnamed2', 'mount', 'Disk']


df=df.reset_index()
df=df.iloc[1:]
df=df.fillna(method='ffill')

df=df.join(df['Disk'].str.split(' ', expand=True))

df.columns= ['server_index', 'Sr_No', 'Device_Name',    'Device_Ip', 'Memory_min', 'Memory', 'memory_avg', 'memory_total', 'Unnamed1', 'CPU_min', 'CPU', 'CPU_avg',     'Unnamed2', 'mount', 'Disk', 'consumed', 'separator',                      'total', 'separator2', 'percent']


df=df.dropna(axis=0, how='all')
df=df.dropna(axis=1, how='all')

df['percent'] = df['percent'].str.replace('[', '').str.replace(']', '').str.replace('%', '').astype(float)

df.sort_values('percent', ascending=False).head(2)
df['Memory_min'] = df['Memory_min'].str.replace('%', '').astype(float)
df['Memory'] = df['Memory'].str.replace('%', '').astype(float)
df['memory_avg'] = df['memory_avg'].str.replace('%', '').astype(float)
df['CPU_min'] = df['CPU_min'].str.replace('%', '').astype(float)
df['CPU'] = df['CPU'].str.replace('%', '').astype(float)
df['CPU_avg'] = df['CPU_avg'].str.replace('%', '').astype(float)
df=df.replace('GB$|MB$', '', regex=True)
df['memory_total'] = df['memory_total'].astype(float) / 1000
df['memory_total'] = df['memory_total'].astype(int)

df.columns = ['server_id', 'Sr_No', 'Device_Name', 'Memory_min_percent', 'Memory_percent', 'memory_avg_percent',
       'memory_total_GB', 'CPU_min_percent', 'CPU_percent', 'CPU_avg_percent', 'mount', 'Disk',
       'consumed_GB', 'separator', 'total_disk_GB', 'separator2', 'disk_full_percent']

now = pd.datetime.now()
myfilename='esds'+now.strftime("%d%B%Y")+'.xlsx'

df.to_excel(myfilename,  encoding="ISO-8859-1", index=False)

s3 = boto3.resource('s3', aws_access_key_id=MY_ACCESS_KEY_ID, aws_secret_access_key=MY_SECRET_ACCESS_KEY, region_name='us-east-1')
BUCKET = "gmailfiles"
s3.Bucket(BUCKET).upload_file(myfilename, 'esds/'+str(myfilename))


df['record_created'] = pd.datetime.now()
df=df.astype(str)
df['dynamodb'] = df['record_created'] + ':' + df['Device_Name'] + df['mount']

df=df.replace('', '0')
df=df.astype(str)

myl=df.T.to_dict().values()

resource = boto3.resource('dynamodb', aws_access_key_id=MY_ACCESS_KEY_ID, aws_secret_access_key=MY_SECRET_ACCESS_KEY, region_name='us-east-1')

table = resource.Table('esds1')

for student in myl:
    table.put_item(Item=student)

