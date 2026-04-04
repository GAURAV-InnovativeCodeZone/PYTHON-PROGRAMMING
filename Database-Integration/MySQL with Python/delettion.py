from connection import get_connection

conn = get_connection()
db_cursor = conn.cursor()

# Data deletion
delete_query = "DELETE FROM mytable WHERE name = %s"
delete_values = ("balram",)

db_cursor.execute(delete_query, delete_values)
conn.commit()

print(f"{db_cursor.rowcount} Record deleted !...")
