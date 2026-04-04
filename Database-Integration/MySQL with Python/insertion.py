from connection import get_connection

conn = get_connection()
db_cursor = conn.cursor()

# # Single data insertion
# db_cursor.execute("INSERT INTO mytable (name, age) VALUES (%s, %s)", ("Gaurav", 23))
# conn.commit()

# Multiple data insertion
query = "INSERT INTO mytable (name, age) VALUES (%s, %s)"
values = [("Gaurav", 23),
          ("Aditya", 22),
          ("Ajay", 21),
          ("Balram", 24)
]
db_cursor.executemany(query, values)
conn.commit()

print(db_cursor.rowcount,"Data inserted !...")

