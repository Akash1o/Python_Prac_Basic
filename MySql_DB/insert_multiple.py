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

sql= "insert into user(name,age,email) values(%s,%s,%s)"

val=[

    ("akash",123,"akash@gmail.com"),
     ("sandehs",122,"sandesh@gmail.com"),
    ("ankit",21,"ankith@gmail.com")

]

cursor.executemany(sql,val)

conn.commit()

print(cursor.rowcount,"items inserted succesfully.")
