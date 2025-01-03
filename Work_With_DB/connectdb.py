import sqlite3

#connect to database( if not exist , it will create 
# automatically.)

conn =sqlite3.connect('mydatabase.db')

print("database is connected")

#curson object to excute sql commands.
cursor = conn.cursor()

#creating table
cursor.execute('''
CREATE TABLE IF NOT EXISTS users(
     id INTEGER PRIMARY KEY AUTOINCREMENT,
    name TEXT NOT NULL,
    age INTEGER
          
               )
       '''   )

print("table created")

conn.commit() #commit the changes

conn.close()  #close the connection