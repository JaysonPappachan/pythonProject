import mysql.connector

mydb = mysql.connector.connect(host="localhost", user="Jayson", passwd="Password@123", database="JaysonDB")

mycursor = mydb.cursor()

mycursor.execute("select * from student")

for i in mycursor:
    print(i)