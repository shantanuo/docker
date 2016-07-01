### elasticsearch with kibana accessible from any IP 

docker run -d  -p 9200:9200 -p 5601:5601 shantanuo/elasticsearch

### Make sure that you have allocated enough disk for containers

Check the Data Space Total and if it is default 107.4 GB then increase it by editing config file

docker info | grep Space

Modify the options line and add 

vi /etc/sysconfig/docker 

-g /var/lib/docker --storage-opt dm.basesize=700G --storage-driver=devicemapper 
_____

rm -rf /var/lib/docker/

mkdir -p /var/lib/docker/devicemapper/devicemapper

dd if=/dev/zero of=/var/lib/docker/devicemapper/devicemapper/data bs=1G count=0 seek=250


#### disable replication and limit number of shards

curl -XPUT 'localhost:9200/enwiki_content' -d '
{
    "settings": {
        "index" : {
            "number_of_shards" : 1,
            "number_of_replicas" : 0
        }
    }
}
'


## Download wikipedia data

### test with 50 MB JSON file

time wget https://dumps.wikimedia.org/other/cirrussearch/20160502/emlwiki-20160502-cirrussearch-content.json.gz

time gunzip emlwiki-20160502-cirrussearch-content.json.gz

time curl -s -XPOST localhost:9200/wikipedia_content/somelan/_bulk --data-binary @emlwiki-20160502-cirrussearch-content.json


### This is 31 GB compressed english wikipedia 

wget https://s3.amazonaws.com/oksoft/enwiki-20160502-cirrussearch-general.json.gz

time gunzip enwiki-20160502-cirrussearch-general.json.gz

time curl -s -XPOST localhost:9200/wikipedia_content/somelan/_bulk --data-binary @enwiki-20160502-cirrussearch-general.json

#### Or use parallel for faster load
time zcat enwiki-20160502-cirrussearch-general.json.gz | parallel --pipe -L 2 -N 2000 -j3 'curl -s http://localhost:9200/enwiki_content/_bulk --data-binary @- > /dev/null'

##### It will take around 24 hours to load more than 2 Crore records (2,52,46,582)

## Connect to ES
### Check the indexes

curl 'localhost:9200/_cat/indices?v'

### python code to connect

import elasticsearch

es = elasticsearch.Elasticsearch('http://52.87.253.190')

res = es.search(index="wikipedia_content", body={"query": {"match_all": {}}})

print("Got %d Hits:" % res['hits']['total'])

### Kibana access

http://52.87.253.190:5601/
