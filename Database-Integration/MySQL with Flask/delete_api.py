from flask import Flask, request
from connect import get_db_connection

app = Flask(__name__)

# DELETE API to remove data from database
 
@app.route('/delete_employee/<int:id>', methods=['DELETE'])
def delete_employee(id):
    conn = get_db_connection()
    cursor = conn.cursor()

    query = "DELETE FROM employees WHERE id=%s"
    cursor.execute(query, (id,))
    conn.commit()

    return {"message": "Employee deleted successfully"}

if __name__ == '__main__':
    app.run(debug=True)
