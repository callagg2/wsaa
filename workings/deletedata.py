# deleting data from a database
#author: Gerry Callaghan

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa1"
)

mycursor = mydb.cursor()
sql = "Delete from books1 where id = %s"
values = (1,)

mycursor.execute(sql, values)

mydb.commit()

print("1 record deleted")
mycursor.close()
mydb.close()