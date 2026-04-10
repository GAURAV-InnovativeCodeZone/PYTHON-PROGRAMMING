from flask import Blueprint, request
from db import get_db_connection
from utils.response import success, error

employee_bp = Blueprint('employee', __name__)


# GET API TO FETCH ALL EMPLOYEES
@employee_bp.route('/employees', methods=['GET'])
def get_employees():
    """
    Get all employees
    ---
    responses:
      200:
        description: List of employees
    """
    try:
        conn = get_db_connection()
        cursor = conn.cursor(directory=True)
        
        cursor.execute("SELECT * FROM employees")
        data = cursor.fetchall()
        
        return success("Employees fetched successfully", data)
    
    except Exception as e:
        return error(str(e), 500)
    
# POST API TO ADD A NEW EMPLOYEE
@employee_bp.route('/add-employee', methods=['POST'])
def add_employee():
    """
    Add a new employee
    ---
    parameters:
      - name: body
        in: body
        required: true
        schema:
          type: object
          properties:
            name:
              type: string
            email:
              type: string
            salary:
              type: integer
    responses:
      201:
        description: Employee created
    """
    data = request.get_json()

    if not data:
        return error("No data provided")

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    if not name or not email or not salary:
        return error("All fields required")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, salary))
        conn.commit()

        return success("Employee added", status=201)

    except Exception as e:
        return error(str(e), 500)
    

# PUT API TO UPDATE EMPLOYEE DETAILS
@employee_bp.route('/update-employee/<int:id>', methods=['PUT'])
def update_employee(id):
    data = request.get_json()

    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')

    if not name or not email or not salary:
        return error("All fields required")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "UPDATE employees SET name=%s, email=%s, salary=%s WHERE id=%s"
        cursor.execute(query, (name, email, salary, id))
        conn.commit()

        if cursor.rowcount == 0:
            return error("Employee not found", 404)

        return success("Employee updated")

    except Exception as e:
        return error(str(e), 500)
    
# PATCH API TO UPDATE EMPLOYEE DETAILS
@employee_bp.route('/patch-employee/<int:id>', methods=['PATCH'])
def patch_employee(id):
    data = request.get_json()

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
        return error("No fields to update")

    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = f"UPDATE employees SET {', '.join(fields)} WHERE id=%s"
        values.append(id)

        cursor.execute(query, tuple(values))
        conn.commit()

        return success("Employee updated partially")

    except Exception as e:
        return error(str(e), 500)
    
# DELETE API TO DELETE AN EMPLOYEE
@employee_bp.route('/delete-employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        query = "DELETE FROM employees WHERE id=%s"
        cursor.execute(query, (id,))
        conn.commit()

        if cursor.rowcount == 0:
            return error("Employee not found", 404)

        return success("Employee deleted")

    except Exception as e:
        return error(str(e), 500)
    
