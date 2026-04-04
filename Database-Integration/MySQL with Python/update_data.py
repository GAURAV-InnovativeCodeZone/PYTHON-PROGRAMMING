from connection import get_connection

conn = get_connection()
db_cursor = conn.cursor()

# Update data
update_query = "UPDATE mytable SET name = %s WHERE age = %s"
update_values = ("Balram", 22)
db_cursor.execute(update_query, update_values)
conn.commit()

print(f"{db_cursor.rowcount} rows updated !...")
