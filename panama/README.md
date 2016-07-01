run the docker container that has sqlite and panama db pre-installed

docker run -it shantanuo/panamapapers /bin/sh

start sqlite

sqlite3 panama.sqlite

and then at sqlite prompt...

sqlite> select * from panama limit 10;

