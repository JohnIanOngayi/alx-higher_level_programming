#!/usr/bin/python3

"""
Module queries a db to list all cities of a state
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
        f"""
        SELECT cities.name FROM cities
        WHERE state_id =
        (SELECT id FROM states
        WHERE name = %s)
        """,
        (sys.argv[4],)
    )

    result = []
    rows = c.fetchall()
    for eachRow in rows:
        result.append(eachRow[0])

    for _ in range(0, len(result)):
        if (_ < len(result)-1):
            print(result[_], end=', ')
        else:
            print(result[_], end='')
    print()

    c.close()
    conn.close()
