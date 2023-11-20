import mysql.connector

# Port 3306 behöver vi inte ange = standard för MySQL

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="1234",
  database="northwind",
  port = 50000
)
mycursor = mydb.cursor()

# INSERT INTO northwind.Categories
# (CategoryID, CategoryName, Description, Picture)
# VALUES(0, '', '', ?);

sql = "INSERT INTO northwind.Categories (CategoryID, CategoryName, Description, Picture) VALUES (%s, %s, %s, %s)"
val = (0,'Energy bar', 'I have the power', '')

# sql = "INSERT INTO movies (title,release_year,genre,instock) VALUES (%s, %s, %s, %s)"
# val = ("Udda eller jämnt", 1971,"Drama", 12)
mycursor.execute(sql, val)
  
mydb.commit()