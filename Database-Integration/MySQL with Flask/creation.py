from connect import get_db_connection
from flask import Flask

app = Flask(__name__)

conn = get_db_connection()
cursor = conn.cursor()

# Database creation
cursor.execute("CREATE DATABASE company_db")
cursor.execute("USE company_db")
print("Database created !...")


# Table creation
cursor.execute("""
    CREATE TABLE employees (
    id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(100),
    email VARCHAR(100),
    salary INT
)
""")
print("Table created!")

# cursor.execute ("INSERT INTO employees (id, name, email, salary) VALUES (5,'Gautam', 'gautam@email.com', 20000)")
# conn.commit();

# cursor.execute ("ALTER TABLE employees AUTO_INCREMENT = 5");

# Show databases
# cursor.execute("SHOW DATABASES")
# for db in cursor:
#     print("List of databases :", db)
    

# Show Tables
# cursor.execute("SHOW TABLES")
# for tb in cursor:
#     print("Tables in database :", tb)


# db_cursor.execute("RENAME TABLE employee to mytable2")
# print("Table renamed !...")

# db_cursor.execute("DROP TABLE mytable2")
# print("Table deleted !...")



