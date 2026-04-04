import mysql.connector

conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aura@123",
        database="mydb"
)
db_cursor = conn.cursor()

# Table creation
# db_cursor.execute("CREATE TABLE mytable(name VARCHAR(20), age int)")
# print("Table created !...")

db_cursor.execute("SHOW TABLES")
for tb in db_cursor:
    print("Tables in database :", tb)

# db_cursor.execute("RENAME TABLE employee to mytable2")
# print("Table renamed !...")

# db_cursor.execute("DROP TABLE mytable2")
# print("Table deleted !...")
