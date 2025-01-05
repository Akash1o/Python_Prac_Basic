import mysql.connector

conn = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database ="python_test"

)

if conn.is_connected():
    print("connected to db")
    cursor= conn.cursor()
     
cursor.execute("select *from user")


result =cursor.fetchall()
#etches all rows returned by the SQL query as a list of tuples.

for x in result:
    print(x)