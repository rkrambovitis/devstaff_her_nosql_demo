#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
from cassandra.policies import RetryPolicy
import os
import sys

if "CASSANDRA_PASS" in os.environ:
   auth_provider = PlainTextAuthProvider(username='devstaff', password=os.environ["CASSANDRA_PASS"])
else:
   print "Please set CASSANDRA_PASS"
   sys.exit()

envhosts=os.getenv('CASSANDRA_HOSTS', "localhost")
hosts=envhosts.split(",")

cluster = Cluster(hosts, auth_provider=auth_provider)
session = cluster.connect('demoks')

if len(sys.argv) > 1:
   num=int(sys.argv[1])
else:
   q = SimpleStatement("SELECT MAX(number) FROM numbers", consistency_level=ConsistencyLevel.ONE)
   r = session.execute(q)
   num = r[0][0]

q = SimpleStatement("SELECT number, value FROM numbers WHERE number = %s", consistency_level=ConsistencyLevel.ONE)
r = session.execute(q, [num])
print r[0][0], r[0][1]
