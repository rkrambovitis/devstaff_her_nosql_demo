#!/usr/bin/python
from cassandra.cluster import Cluster
from cassandra.auth import PlainTextAuthProvider
from cassandra import ConsistencyLevel
import os
import sys

if "CASSANDRA_PASS" in os.environ:
   auth_provider = PlainTextAuthProvider(username='devstaff', password=os.environ["CASSANDRA_PASS"])
else:
   print "Please set CASSANDRA_PASS"
   sys.exit

cluster = Cluster(['192.168.10.235'], auth_provider=auth_provider)
session = cluster.connect('demoks')

#session.execute("CREATE TABLE numbers (number varint PRIMARY KEY, value varchar)")
#session.execute("DROP TABLE numbers")

q=session.execute("SELECT MAX(number) FROM numbers")
number=q[0][0]

query = session.prepare("INSERT INTO numbers (number, value) VALUES (?, ?)")
query.consistency_level = ConsistencyLevel.QUORUM
while True:
   number += 1
   try:
      session.execute_async(query, [number, "foobar"])
      if number%1000 == 0:
         print number
   except KeyboardInterrupt:
      print "Exiting, Please wait... "
      session.execute(query, [number, "foobar"])
      print number
      sys.exit()

