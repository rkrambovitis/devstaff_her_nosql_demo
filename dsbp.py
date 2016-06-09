#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
from cassandra.query import BatchStatement
import os
import sys
import md5

#if "CASSANDRA_PASS" in os.environ:
#   auth_provider = PlainTextAuthProvider(username='devstaff', password=os.environ["CASSANDRA_PASS"])
#else:
#   print "Please set CASSANDRA_PASS"
#   sys.exit

envhosts=os.getenv('CASSANDRA_HOSTS', "localhost")
hosts=envhosts.split(",")

#cluster = Cluster(hosts, auth_provider=auth_provider)
cluster = Cluster(hosts)
session = cluster.connect('demoks')
number=0

#session.execute("DROP TABLE numbers")
#session.execute("CREATE TABLE numbers (number varint PRIMARY KEY, value varchar)")

#q=session.execute("SELECT MAX(number) FROM numbers")
#number=q[0][0]

if len(sys.argv) > 1:
   number=int(sys.argv[1])

if len(sys.argv) > 2:
   end = int(sys.argv[2])
else:
   end = 999999999


query = session.prepare("INSERT INTO numbers (number, value) VALUES (?, ?)")
query.consistency_level = ConsistencyLevel.ONE

while number < end:
   foo = md5.new(str(number)).hexdigest()
   line = (foo +" "+ foo + " " + foo + " " + foo + " " + foo)
   batch = BatchStatement(consistency_level=ConsistencyLevel.ONE)
   try:
      batch.add(query, (number, line))
      if number%1000 == 0:
         session.execute(batch)
         print number
         batch = BatchStatement(consistency_level=ConsistencyLevel.ONE)

   except KeyboardInterrupt:
      print "Exiting, Please wait... "
      session.execute(query, [number, line])
      print number
      sys.exit()
   number += 1
session.execute(query, [number, line])
