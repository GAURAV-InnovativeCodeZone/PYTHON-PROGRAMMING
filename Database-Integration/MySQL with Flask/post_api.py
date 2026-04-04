from flask import Flask, request
from connect import get_db_connection

app = Flask(__name__)

# POST API to insert data into database

@app.route('/add_employee', methods=['POST'])
def add_employee():
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)"
    cursor.execute(query, (name, email, salary))
    conn.commit()

    return {"message": "Employee added successfully"}

if __name__ == '__main__':
    app.run(debug=True)
