#!/usr/bin/python3
"""takes in the name of a state as an argument and lists all cities"""
import MySQLdb
import sys


if __name__ == '__main__':
    db = MySQLdb.connect(host="localhost", user=sys.argv[1],
                         passwd=sys.argv[2], db=sys.argv[3])
    cur = db.cursor()
    cur.execute("SELECT cities.name FROM cities, states "
                "WHERE states.id = cities.state_id AND states.name = %s "
                "ORDER BY cities.id", (sys.argv[4], ))
    rows = cur.fetchall()
    print(", ".join([row[0] for row in rows]))
    cur.close()
    db.close()
