Use these commands:

docker run -p 9200:9200 -p 5601:5601 -v /tmp/:/tmp/ -d shantanuo/es3

cd /home/elasticsearch/elasticsearch-learning-to-rank/demo/

python prepare.py

python index_ml_tmdb.py

python train.py

python search.py rambo

# https://github.com/o19s/elasticsearch-learning-to-rank/tree/master/demo
