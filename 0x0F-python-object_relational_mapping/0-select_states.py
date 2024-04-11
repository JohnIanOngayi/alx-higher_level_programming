#!/usr/bin/python3

"""
Module queries a db to list all states
"""

if __name__ == "__main__":
    import MySQLdb
    import sys

    conn = MySQLdb.connect(
        host="localhost",
        user=sys.argv[1],
        password=sys.argv[2],
        database=sys.argv[3],
        port=3306
    )

    c = conn.cursor()
    c.execute(
        """
        SELECT * from states
        ORDER BY states.id
        """
    )

    rows = c.fetchall()
    for eachRow in rows:
        print(eachRow)
    c.close()
    conn.close()
