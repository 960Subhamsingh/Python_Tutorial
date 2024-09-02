import cx_Oracle
con = cx_Oracle.connect('system/tiger@localhost:1521/xe')

cur = con.cursor()

cur.execute('select * from employee')

row = cur.fetchone()
print(row)


# for i in cur.fetchone():
#     print(i)


res = cur.callfunc('myfunc', cx_Oracle.NUMBER, ('abc', 2) )

print(res)