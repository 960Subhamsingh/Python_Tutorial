# import library 
import cx_Oracle

# connect databases
con = cx_Oracle.connect('system/tiger@localhost:1521/xe')

cur = con.cursor()

cur.execute('select * from employee')

res = cur.fetchmany()
print(res)
 

