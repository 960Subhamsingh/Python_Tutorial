import cx_Oracle
 
# Create a table in Oracle database
try:
##    conn_str = 'user/password@host:port/service_name'
    con = cx_Oracle.connect('system/tiger@localhost:1521/xe')
    
    print(con.version)
 
    # Now execute the sqlquery
    cursor = con.cursor()
 
    # Creating a table employee
    exe=cursor.execute("create table employee(empid integer primary key, name varchar2(30), salary number(10, 2))")
    
    print("Table Created successfully")
 
except cx_Oracle.DatabaseError as e:
    print("There is a problem with Oracle", e)
 
# by writing finally if any error occurs
# then also we can close the all database operation
finally:
    if cursor:
        cursor.close()
    if con:
        con.close()


## second method

def create_usertable():
    cursor.execute('CREATE TABLE  userstable(username TEXT,password TEXT)')


def add_userdata(username,password):
	cursor.execute('INSERT INTO userstable(username,password) VALUES (?,?)',(username,password))
	conn.commit()

def login_user(username,password):
	cursor.execute('SELECT * FROM userstable WHERE username =? AND password = ?',(username,password))
	data = cursor.fetchall()
	return data

    
