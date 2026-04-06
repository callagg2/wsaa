import mysql.connector

db = mysql.connector.connect(
host = "localhost",
user ="root",
password ="", # this is the password for the database, if you have one, if not, leave it blank
database = "wsaa1" 
)

cursor = db.cursor() # this is where the data is stored when read from the database

#cursor.execute("create database wsaa1") # this is how you create a database, if it doesn't exist already

#sql= "CREATE TABLE books1 (id INT AUTO_INCREMENT PRIMARY KEY, title VARCHAR(255), author VARCHAR(255), price INT)"
sql = "insert into books1 (title, author, price) values (%s, %s, %s)" # this is the sql statement to insert data into the database, the %s are placeholders for the values that will be inserted
values = ("The Great Gatsby", "F. Scott Fitzgerald", 10)

cursor.execute(sql, values)

db.commit() # this is to save the changes to the database, if you don't do this, the changes won't be saved
print ("1 record inserted, ID:", cursor.lastrowid) # this is to print the id of the last record that was inserted
'''
# now to work with the data
results = cursor.fetchall() # (so it grabs everything)
for result in results:
	print (result)
'''
cursor.close()
db.close()  #if you don't close this, you can get resource leaks, you could run out of connections