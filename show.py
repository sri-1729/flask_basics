import psycopg2
import csv
import pandas as pd
import sys

def roll(st, sem):
	f1 = open(f"S{sem}.csv")
	#conn = psycopg2.connect("dbname=students")
	#cur = conn.cursor()
#	cur.execute(f"select * from list where roll = '{st}'")
#	li = cur.fetchall()
	ret = []
	r = csv.reader(f1)
	for i in r:
		if(i[2] == st):
			rank = int(float(i[4]))
			grade = i[3]
			name = i[1]
			ret.append(name)
			ret.append(rank)
			ret.append(grade)
	return ret


