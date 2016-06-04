# devstaff_her_nosql_demo

## Docker HOWTO ##
```
docker run -ti \
-e CASSANDRA_HOSTS="localhost,someother.host" \
-e CASSANDRA_PASS='something' \
rkrambovitis/devstaff-cassandra-demo put

docker run -ti \
-e CASSANDRA_HOSTS="localhost,someother.host" \
-e CASSANDRA_PASS='something' \
rkrambovitis/devstaff-cassandra-demo get 123

docker run -ti rkrambovitis/devstaff-cassandra-demo sh
```
