# devstaff_her_nosql_demo

## Docker HOWTO ##
```
docker run -ti \
-e CASSANDRA_HOSTS="localhost,someother.host" \
-e CASSANDRA_PASS='something' \
rkrambovitis/devstaff-cassandra-demo put <startNum> <endNum>

docker run -ti \
-e CASSANDRA_HOSTS="localhost,someother.host" \
-e CASSANDRA_PASS='something' \
rkrambovitis/devstaff-cassandra-demo get <rangeMin> <rangeMan> <sampleCnt>

docker run -ti rkrambovitis/devstaff-cassandra-demo sh
```
