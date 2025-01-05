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


    #sql query to insert data

    sql= "insert into user(name,age,email) values(%s,%s,%s)"
    val= ("sabin",20,"sabin@gmail.com")

    #excute the query
    cursor.execute(sql,val)

    #commit the changes >
    conn.commit()

    print(f"{cursor.rowcount} record inserted successfully ")

    #close the connection to db and cursor
    cursor.close()
    conn.close()


 