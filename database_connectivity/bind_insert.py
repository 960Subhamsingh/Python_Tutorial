# import cx_Oracle library
import cx_Oracle

# connect Oracle database 
con = cx_Oracle.connect('system/tiger@localhost:1521/xe')

# row and column data in the list form to insert in a orcale table 
# table is mtab 
rows = [ (1, "First" ),
         (2, "Second" ),
         (3, "Third" ),
         (4, "Fourth" ),
         (5, "Fifth" ),
         (6, "Sixth" ),
         (7, "Seventh" ) ]

cur = con.cursor()

cur.bindarraysize = 7

cur.setinputsizes(int, 20)

# insert the data in table of rows variable 
cur.executemany("insert into mtab(id , data) values (:1, :2)", rows)

# commit function are save the mtab 
con.commit()

cur2 = con.cursor()

# select all the data of  mtab
cur2.execute('select * from mtab')

# display all the data in for loop
for i in cur2.fetchall():
    print(i)





