#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from cassandra.query import SimpleStatement
from cassandra.policies import RetryPolicy
import os
import sys
import md5
import random

if "CASSANDRA_PASS" in os.environ:
   auth_provider = PlainTextAuthProvider(username='devstaff', password=os.environ["CASSANDRA_PASS"])
else:
   print "Please set CASSANDRA_PASS"
   sys.exit()

envhosts=os.getenv('CASSANDRA_HOSTS', "localhost")
hosts=envhosts.split(",")

cluster = Cluster(hosts, auth_provider=auth_provider)
session = cluster.connect('demoks')

num=1
if len(sys.argv) < 4:
   print "Usage: %s <rangeMin> <rangeMax> <sampleCnt>" % sys.argv[0]
   sys.exit()

rangeMin=int(sys.argv[1])
rangeMax=int(sys.argv[2])
sampleCnt=int(sys.argv[3])

q = SimpleStatement("SELECT number, value FROM numbers WHERE number = %s", consistency_level=ConsistencyLevel.LOCAL_ONE)

results = []
for x in range(0, sampleCnt):
   num = random.randint(rangeMin, rangeMax)
   results.append(session.execute_async(q, [num]))

for res in results:
   r = res.result()
   print "Cassandra ", r[0][0], r[0][1]
   print "Calculate ", r[0][0], md5.new(str(r[0][0])).hexdigest()
   print

#r = session.execute("SELECT number, value FROM numbers")
#for row in r:
#   print row[0], row[1]
