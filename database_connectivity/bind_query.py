import cx_Oracle

con = cx_Oracle.connect('system/tiger@localhost:1521/xe')

cur = con.cursor()
cur.prepare('select * from emp where deptno = :id')

cur.execute(None, {'id': 30})
for i in  cur.fetchall():
    print(i)

