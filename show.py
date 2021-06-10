import psycopg2
import csv
import pandas as pd
import sys

def roll(st):
	f1 = open("res.csv")
	conn = psycopg2.connect("dbname=students")
	cur = conn.cursor()
	cur.execute(f"select * from list where roll = '{st}'")
	li = cur.fetchall()
	r = csv.reader(f1)
	for i in r:
		if(i[1] == st):
			rank = i[3]
			grade = i[2]
	ret = []
	if(len(li) != 0):
		ret.append(li[0][2])
		ret.append(str(li[0][0]))
		ret.append(rank)
		ret.append(grade)
		cur.close()
		conn.commit()
	return ret


