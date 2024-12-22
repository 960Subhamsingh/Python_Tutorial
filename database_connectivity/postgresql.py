import psycopg2

conn = psycopg2.connect(dbname="subham", host="localhost" , user="postgres", password="tiger", port = 5432)

cur = conn.cursor()

conn.commit()
cur.close()
conn.close()