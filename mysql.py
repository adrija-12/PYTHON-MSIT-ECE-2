#Create Database
import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="msit"
)

cursor=mydb.cursor()