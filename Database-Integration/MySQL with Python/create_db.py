from connection import get_connection

conn = get_connection()
db_cursor = conn.cursor()

# Database creation
db_cursor.execute("CREATE DATABASE mydb")
print("Database created !...")

db_cursor.execute("SHOW DATABASES")
for db in db_cursor:
    print("Tables in database :", db)