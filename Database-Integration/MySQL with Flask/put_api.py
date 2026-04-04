from flask import Flask, request
from connect import get_db_connection

app = Flask(__name__)

# PUT API to update data in database

@app.route('/update_employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    conn = get_db_connection()
    cursor = conn.cursor()

    query = "UPDATE employees SET name=%s, email=%s, salary=%s WHERE id=%s"
    cursor.execute(query, (name, email, salary, id))
    conn.commit()

    return {"message": "Employee updated successfully"}

if __name__ == "__main__":
    app.run(debug=True)
    