import mysql.connector

def get_db_connection():
    return mysql.connector.connect(
        host = "localhost",
        user ="root",
        password = "aura@123",
        database = "company_db"
    )

if __name__ == '__main__':
    print("Database connected successfully !...")
    