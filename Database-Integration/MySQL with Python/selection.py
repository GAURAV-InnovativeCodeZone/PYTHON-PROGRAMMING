from connection import get_connection

conn = get_connection()
db_cursor = conn.cursor()

# Data selection or fetching or read
db_cursor.execute("SELECT * FROM mytable")
for row in db_cursor.fetchall():
    print(row)
    
# select_data = db_cursor.fetchall()
# print(select_data)
