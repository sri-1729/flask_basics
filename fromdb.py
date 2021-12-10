import psycopg2
import pandas as pd

conn = psycopg2.connect("dbname=students user=srijith")
curr = conn.cursor()

sql = f"SELECT l.name, l.roll, r.grade FROM s4res AS r, list AS l WHERE l.roll = r.roll ORDER BY r.grade DESC"
curr.execute(sql)
res = curr.fetchall()

df = pd.DataFrame(res)
df['rank'] = df[2].rank(ascending = False, method='min')
df['rank'].astype(int)

df.to_csv("S4.csv")


