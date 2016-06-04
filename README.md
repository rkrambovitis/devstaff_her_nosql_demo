# devstaff_her_nosql_demo

## Docker HOWTO ##
```
docker build -t dsgp .
docker run -ti -e CASSANDRA_PASS='something' dsgp put
docker run -ti -e CASSANDRA_PASS='something' dsgp get
```

## HOWTO ##
```
pip install cassandra-driver
export CASSANDRA_PASS=whatever
./dsp.py
ctrl+c to exit

./dsg.py
```

