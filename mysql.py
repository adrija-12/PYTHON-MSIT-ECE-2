#Create Database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

cursor=mydb.cursor()
abc.execute("CREATE DATABASE msit")
print("Database Created Successfully")
In [2]:
#Create Table
import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mysql_query = db.cursor()

mysql_query.execute("CREATE TABLE customers_students(id INT AUTO_INCREMENT PRIMARY KEY,name VARCHAR(255), address VARCHAR(255), email VARCHAR(100), gender TEXT(50))")
print("Table Created Successfully")

#Data Insert in Table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
val = ("Mainak", "Kolkata")
mycursor.execute(sql, val)

sql_2= "INSERT INTO customers_students (name, address,email,gender) VALUES (%s, %s,%s, %s)"
val_2 = ("Test1", "addressTest","test@gmail.com","Male")
mycursor.execute(sql_2, val_2)

mydb.commit()

print(mycursor.rowcount, "record inserted.")

#Data Insert in Table
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
a=str(input("Enter your name -> "))
b=str(input("Enter your address -> "))
val = (a, b)
mycursor.execute(sql, val)

sql_2= "INSERT INTO customers_students (name, address,email,gender) VALUES (%s, %s,%s, %s)"
a=str(input("Enter your name ->"))
b=str(input("Enter your address ->  "))
c=str(input("Enter your email"))
d=str(input("Enter your gender -> "))
val_2=(a,b,c,d)
mycursor.execute(sql_2, val_2)
mydb.commit()
print(mycursor.rowcount, "record inserted.")

#fetch data
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers_students")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)


#Search Data
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

mycursor = mydb.cursor()

sql = "SELECT * FROM customers_students WHERE email = 'test@gmail.com'"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)

