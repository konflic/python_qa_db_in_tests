# Using database with testing

## Connect to mysql/mariadb database

Python DB API - https://www.python.org/dev/peps/pep-0249/

# Libs

- https://pypi.org/project/mysql-connector-python/

## Basics

1) Create connection.


```python
import mysql.connector

# Connect to server and database
connection = mysql.connector.connect(
    host="127.0.0.1",
    port=3306,
    user="mike",
    password="s3cre3t!",
    database="employees"
)

# Getting cursor from connection
cursor = connection.cursor()
```


2) CRUD

```python
cursor.execute("SELECT CURDATE()")
row = cursor.fetchone()

sql = "INSERT INTO {DB_NAME} (name, email, phone, address) VALUES (?, ?, ?, ?)".format(DB=DB_NAME)
data = ("Vasiliy", "vasiliy@mail.ru", "+7999999999", "Moscow")
connection.execute(sql, data)
connection.commit()
```


3) Close

```python
connection.close()
```
