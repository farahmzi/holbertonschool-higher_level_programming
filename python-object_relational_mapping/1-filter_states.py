#!/usr/bin/python3
"""Lists states starting with 'N' from hbtn_0e_0_usa, ordered by id."""

import sys
import MySQLdb


def main():
    """Connect to MySQL and print (id, name) for matching states."""
    user, passwd, dbname = sys.argv[1], sys.argv[2], sys.argv[3]

    conn = MySQLdb.connect(
        host="localhost",
        port=3306,
        user=user,
        passwd=passwd,
        db=dbname,
        charset="utf8",
    )
    cur = conn.cursor()

    # TODO: Make the predicate case-sensitive for uppercase N
    query = (
        "SELECT id, name FROM states "
        "WHERE "  # <-- fill with condition that matches names starting with uppercase N
        "ORDER BY id ASC;"
    )
    cur.execute(query)

    rows = cur.fetchall()
    for row in rows:
        print(row)

    cur.close()
    conn.close()


if __name__ == "__main__":
    main()
