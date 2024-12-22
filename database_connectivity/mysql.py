import mysql.connector

conn = None

try:
    # Attempt to establish a connection to the MySQL database
    conn = mysql.connector.connect(host="localhost", database="hotal", user="root", password="tiger")

    # Check if the connection is successfully established
    if(conn.is_connected()):
        print("connected to Mysql database")
except mysql.connector.Error as e:
    # Print an error message if a connection error occurs
    print(e)

finally:
    # Close the database connection in the 'finally' block to ensure it happens
    if(conn is not None and conn.is_connected():
       conn.close()
       
