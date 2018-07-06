#!/usr/bin/env python3

import psycopg2
from pprint import pprint

conn = psycopg2.connect("dbname=weather user=postgres password=hassan host=localhost")
cur = conn.cursor()
cur.execute("INSERT INTO cities VALUES('05/08/2017', 'Sydney', '16')")
cur.execute("SELECT date, city_name, averagetemp_celsius from cities")
rows = cur.fetchall()
conn.commit()
cur.close()
conn.close()
