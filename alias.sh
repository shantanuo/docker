mkdir -p /my/custom

cat << here_doc > /my/custom/config-file.cnf 
[mysqld]
myisam_sort_buffer_size = 34G
tmp_table_size=34G
max_heap_table_size=34G
key_buffer_size=34G
here_doc

echo "alias installmysql='docker run -d -p 3306:3306  -e MYSQL_ALLOW_EMPTY_PASSWORD=yes  -v /my/custom:/etc/mysql/conf.d  -v /storage/test-mysql/datadir:/var/lib/mysql mysql:5.5'" >> ~/.bashrc

echo "alias installelastic='docker run --name myelastic -v /tmp/:/usr/share/elasticsearch/config  -p 9200:9200 -p 9300:9300  -e ES_HEAP_SIZE=1g -d elasticsearch'" >> ~/.bashrc

echo "alias installkibana='docker run -d -p 5601:5601 --link myelastic:elasticsearch -e ELASTICSEARCH_URL=http://elasticsearch:9200 kibana'" >> ~/.bashrc

echo "alias installlogstash='docker run -d -v "/tmp/logstash.conf":/usr/local/logstash/config/logstash.conf -v /tmp/:/tmp/ logstash -f /usr/local/logstash/config/logstash.conf'" >> ~/.bashrc

echo "alias installminiconda='docker run -p 7778:7778 -t continuumio/miniconda3 /bin/bash -c \" conda  install -c conda-forge -y geopandas gdal tqdm jupyter && cd /home/ && jupyter notebook --ip=* --port=7778\" ' " >> ~/.bashrc


source ~/.bashrc

#curl -sf -L https://raw.githubusercontent.com/shantanuo/docker/master/alias.sh | sh
