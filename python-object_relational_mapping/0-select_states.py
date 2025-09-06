#!/usr/bin/python3
"""Lists all states from the database hbtn_0e_0_usa sorted by states.id."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and print all states as (id, 'name') tuples."""
    user, passwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=dbname,
        charset="utf8"
    )
    cur = conn.cursor()
    cur.execute("SELECT id, name FROM states ORDER BY id ASC;")
    rows = cur.fetchall()

    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
