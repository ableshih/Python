https://www.itread01.com/content/1549041301.html   
https://ithelp.ithome.com.tw/articles/10215161      
https://jerrynest.io/mysql-tutorial/   


```
https://docs.microsoft.com/zh-tw/azure/mysql/connect-workbench
建立資料表、將資料插入、讀取資料、更新資料、刪除資料

這段程式碼會建立名為 quickstartdb 的空白資料庫，
然後會建立名為 inventory 的範例資料表。 
它會插入 三筆 資料列，
然後讀取資料列。
它會使用 update 陳述式將資料進行變更，並再次讀取資料列。 
最後會刪除資料列，然後再次讀取資料列。

-----------------------------------------------

-- Create a database
-- DROP DATABASE IF EXISTS quickstartdb;
CREATE DATABASE quickstartdb;
USE quickstartdb;

-- Create a table and insert rows
DROP TABLE IF EXISTS inventory;
CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);
INSERT INTO inventory (name, quantity) VALUES ('banana', 150);
INSERT INTO inventory (name, quantity) VALUES ('orange', 154);
INSERT INTO inventory (name, quantity) VALUES ('apple', 100);

-- Read
SELECT * FROM inventory;

-- Update
UPDATE inventory SET quantity = 200 WHERE id = 1;
SELECT * FROM inventory;

-- Delete
DELETE FROM inventory WHERE id = 2;
SELECT * FROM inventory;

-----------------------------------------------
quickstartdb
	Tables
		inventory
			Columns
				id
				name
				quantity				
			Indexes
				PRIMARY
				id
			Foreign Keys
			Triggers
		Views
		Stored Procedures
		Functions

-----------------------------------------------






=====================================================================================
pip install mysql-connector-python

MySQL Connector/Python Developer Guide
https://dev.mysql.com/doc/connector-python/en/


-----------------------------------------------

https://docs.microsoft.com/zh-tw/azure/mysql/connect-python

建立資料表及插入資料
使用下列程式碼搭配 INSERT SQL 陳述式連線至伺服器和資料庫、建立資料表，以並載入資料。
程式碼會匯入 mysql.connector 程式庫，
並使用 connect() 函式搭配 config 集合中的引數連線至適用於 MySQL 的 Azure 資料庫。 
此程式碼使用連線上的資料指標，而 cursor.execute() 方法會對 MySQL 資料庫執行 SQL 查詢。
-----------------------------------------------
import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'<mydemoserver>.mysql.database.azure.com',
  'user':'<myadmin>@<mydemoserver>',
  'password':'<mypassword>',
  'database':'<mydatabase>'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Drop previous table of same name if one exists
  cursor.execute("DROP TABLE IF EXISTS inventory;")
  print("Finished dropping table (if existed).")

  # Create table
  cursor.execute("CREATE TABLE inventory (id serial PRIMARY KEY, name VARCHAR(50), quantity INTEGER);")
  print("Finished creating table.")

  # Insert some data into table
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("banana", 150))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("orange", 154))
  print("Inserted",cursor.rowcount,"row(s) of data.")
  cursor.execute("INSERT INTO inventory (name, quantity) VALUES (%s, %s);", ("apple", 100))
  print("Inserted",cursor.rowcount,"row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")


-----------------------------------------------

讀取資料
使用下列程式碼搭配 SELECT SQL 陳述式來連線和讀取資料。
此程式碼會匯入 mysql.connector 程式庫，並使用 connect() 函式搭配 config 集合中的引數連線至適用於 MySQL 的 Azure 資料庫。 
此程式碼使用連線上的資料指標，而 cursor.execute() 方法會對 MySQL 資料庫執行 SQL 查詢。
此程式碼會使用 fetchall() 方法來讀取資料列，並將結果集保存在集合資料列中，然後使用 for 迭代器對資料列執行迴圈。
-----------------------------------------------
import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'<mydemoserver>.mysql.database.azure.com',
  'user':'<myadmin>@<mydemoserver>',
  'password':'<mypassword>',
  'database':'<mydatabase>'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Read data
  cursor.execute("SELECT * FROM inventory;")
  rows = cursor.fetchall()
  print("Read",cursor.rowcount,"row(s) of data.")

  # Print all rows
  for row in rows:
    print("Data row = (%s, %s, %s)" %(str(row[0]), str(row[1]), str(row[2])))

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")

-----------------------------------------------

更新資料
使用下列程式碼搭配 UPDATE SQL 陳述式來連線和更新資料。
此程式碼會匯入 mysql.connector 程式庫，並使用 connect() 函式搭配 config 集合中的引數連線至適用於 MySQL 的 Azure 資料庫。 
此程式碼使用連線上的資料指標，而 cursor.execute() 方法會對 MySQL 資料庫執行 SQL 查詢。
-----------------------------------------------
import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'<mydemoserver>.mysql.database.azure.com',
  'user':'<myadmin>@<mydemoserver>',
  'password':'<mypassword>',
  'database':'<mydatabase>'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Update a data row in the table
  cursor.execute("UPDATE inventory SET quantity = %s WHERE name = %s;", (200, "banana"))
  print("Updated",cursor.rowcount,"row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")

-----------------------------------------------

刪除資料
使用下列程式碼搭配 DELETE SQL 陳述式來連線和移除資料。
此程式碼會匯入 mysql.connector 程式庫，並使用 connect() 函式搭配 config 集合中的引數連線至適用於 MySQL 的 Azure 資料庫。 
此程式碼使用連線上的資料指標，而 cursor.execute() 方法會對 MySQL 資料庫執行 SQL 查詢。
-----------------------------------------------
import mysql.connector
from mysql.connector import errorcode

# Obtain connection string information from the portal
config = {
  'host':'<mydemoserver>.mysql.database.azure.com',
  'user':'<myadmin>@<mydemoserver>',
  'password':'<mypassword>',
  'database':'<mydatabase>'
}

# Construct connection string
try:
   conn = mysql.connector.connect(**config)
   print("Connection established.")
except mysql.connector.Error as err:
  if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
    print("Something is wrong with the user name or password.")
  elif err.errno == errorcode.ER_BAD_DB_ERROR:
    print("Database does not exist.")
  else:
    print(err)
else:
  cursor = conn.cursor()

  # Delete a data row in the table
  cursor.execute("DELETE FROM inventory WHERE name=%(param1)s;", {'param1':"orange"})
  print("Deleted",cursor.rowcount,"row(s) of data.")

  # Cleanup
  conn.commit()
  cursor.close()
  conn.close()
  print("Done.")

-----------------------------------------------


-----------------------------------------------


-----------------------------------------------




```
