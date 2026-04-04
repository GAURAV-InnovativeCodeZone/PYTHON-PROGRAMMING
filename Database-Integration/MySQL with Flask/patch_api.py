from flask import Flask, request
from connect import get_db_connection

app = Flask(__name__)

# PATCH API to partially update data in database
 
@app.route('/patch-employee/<int:id>', methods=['PATCH'])
def patch_employee(id):
    data = request.get_json()

    conn = get_db_connection()
    cursor = conn.cursor()

    # Build dynamic query
    fields = []
    values = []

    if 'name' in data:
        fields.append("name=%s")
        values.append(data['name'])

    if 'email' in data:
        fields.append("email=%s")
        values.append(data['email'])

    if 'salary' in data:
        fields.append("salary=%s")
        values.append(data['salary'])

    if not fields:
        return {"error": "No fields to update"}

    query = f"UPDATE employees SET {', '.join(fields)} WHERE id=%s"
    values.append(id)

    cursor.execute(query, tuple(values))
    conn.commit()

    return {"message": "Employee partially updated"}

if __name__ == '__main__':
    app.run(debug=True)
