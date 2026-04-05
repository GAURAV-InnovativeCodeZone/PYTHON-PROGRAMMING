from flask import Flask, request
from connect import get_db_connection

app = Flask(__name__)

@app.route('/validation', methods=['POST'])
def validate():
    data = request.get_json()
    if not data:
        return "No data provided", 400
    
    name = data.get('name')
    email = data.get('email')
    salary = data.get('salary')
    
    if not name or not email or not salary:
        return "Missing required fields", 400
    
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        
        query = "INSERT INTO employees (name, email, salary) VALUES (%s, %s, %s)"
        cursor.execute(query, (name, email, salary))
        conn.commit()
        
        return {
            "status": "success",
            "message":"Employee added successfully"
        }, 201
        
    except Exception as e:
        return {
            "status": "error",
            "message": str(e)
        }, 500
        
if __name__ == '__main__':
    app.run(debug=True)