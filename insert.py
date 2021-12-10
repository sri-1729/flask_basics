import psycopg2

conn = psycopg2.connect("dbname=students user=srijith")
curr = conn.cursor()

pro = open('proc', 'r')
lines = pro.readlines()

for line in lines:
	arr = line.split(',')
	curr.execute(f"INSERT INTO s5res(roll, grade) VALUES('{arr[0]}', {float(arr[1])});")

conn.commit()
pro.close()
