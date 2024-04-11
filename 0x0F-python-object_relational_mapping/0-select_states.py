#!/usr/bin/python3

"""
Module queries a db to list all states
"""


import MySQLdb
import sys

conn = MySQLdb.connect("localhost", sys.argv[1], sys.argv[2], sys.argv[3])
c = conn.cursor()
c.execute("SELECT * from states ORDER BY id")
rows = c.fetchall()
for eachRow in rows:
    print(eachRow)
c.close()
conn.close()
