from connect import get_db_connection
from flask import Flask

app = Flask(__name__)

# GET API to fetch data from database

@app.route('/employees', methods=['GET'])
def get_employees():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    cursor.execute("SELECT * FROM employees")
    data = cursor.fetchall()

    return {"employees": data}
    
if __name__ == '__main__':
    app.run(debug=True)
