import mysql.connector

#connect to the mysql server
conn_db = mysql.connector.connect(
    host="localhost",
    user="root",
    password= "",
    database ="python_test"

)

#check the conncetion .

if conn_db.is_connected():
    print("conncetion succesfull")
    cursor = conn_db.cursor()
    #cursor excute the sql commands and it interacts with db.

#   cursor.execute("CREATE DATABASE mydatabase") creatinga new database.


    create_table_query ="""

    create table if not exists user(
     id int auto_increment primary key,
     name varchar(100) not null ,
     age int not null ,
     email varchar(100) not null
    )

"""

#executing the query. 
cursor.execute(create_table_query)

#commit changes to the db.
conn_db.commit()

#closing the cursor and connection.

cursor.close()
conn_db.close()