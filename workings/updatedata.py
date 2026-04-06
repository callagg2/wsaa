# updating data in a database
#author: Gerry Callaghan

import mysql.connector

mydb = mysql.connector.connect(
    host="localhost",
    user="root",
    password="",
    database="wsaa1"
)

mycursor = mydb.cursor()
sql = "Update books1 set title = %s, author = %s, price = %s where id = %s"
values = ("Donata Goes on Holidays", "Happy Gilmore", 14, 2)

mycursor.execute(sql, values)

mydb.commit()

print("1 record updated, ID:", mycursor.lastrowid)
mycursor.close()
mydb.close()
