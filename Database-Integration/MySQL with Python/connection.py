import mysql.connector

def get_connection():
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="aura@123",
        database="mydb"
    )
    return conn

if __name__ == "__main__":
    print("Connection established successfully!...")