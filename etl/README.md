- Download the sample data from:

https://www.kaggle.com/c/kkbox-churn-prediction-challenge/data

- Make sure to change access, secret key. Create or empty S3 bucket for e.g. todel164
- Make sure transactions.csv file is in folder /tmp/predict-customer-churn/data/
```
docker run -v /tmp/predict-customer-churn/data/:/tmp/ \
-e AWS_ACCESS_KEY_ID='xxx' \
-e AWS_SECRET_ACCESS_KEY='xxx' \
-e s3_path='s3://todel164' \
-e csv_path='/tmp/transactions.csv' \
shantanuo/etl python /home/process.py
```

- Create Athena table like this... 
- make sure that the athena column name match with the csv file's first row
```
CREATE EXTERNAL TABLE IF NOT EXISTS sampledb.todel14a (
`msno` string,  
`is_churn` string
)
ROW FORMAT SERDE 'org.apache.hadoop.hive.ql.io.parquet.serde.ParquetHiveSerDe'
WITH SERDEPROPERTIES (
  'serialization.format' = '1'
) LOCATION 's3://todel164/'
TBLPROPERTIES ('has_encrypted_data'='false');
```

- If the csv file is too large, split it.
- make sure that the new files have the same header as original csv

> split -C 1G user_logs.csv

The following shell script can be used to add the headers to each part and export parquet files to S3

```
#!/bin/sh
for file in `ls x*`
do
if [ "$file" == "xaa" ]
then
docker run -v /tmp/predict-customer-churn/data/:/tmp/ \
-e AWS_ACCESS_KEY_ID='xxx' \
-e AWS_SECRET_ACCESS_KEY='xxx' \
-e s3_path='s3://todel164' \
-e csv_path="/tmp/xaa" \
shantanuo/etl python /home/process.py
else
head -1 user_logs.csv > "$file"_temp
cat $file >> "$file"_temp
mv "$file"_temp $file

docker run -v /tmp/predict-customer-churn/data/:/tmp/ \
-e AWS_ACCESS_KEY_ID='xxx' \
-e AWS_SECRET_ACCESS_KEY='xxx' \
-e s3_path='s3://todel164' \
-e csv_path="/tmp/$file" \
shantanuo/etl python /home/process.py

fi
done
```
