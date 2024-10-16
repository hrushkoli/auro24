import mysql.connector

db = mysql.connector.connect(host="localhost",user="root",password="")

myCursor = db.cursor()

myCursor.execute("show Databases")

for i in myCursor:
    print(i)

