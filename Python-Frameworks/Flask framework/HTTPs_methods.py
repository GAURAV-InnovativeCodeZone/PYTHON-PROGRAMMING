# HTTP Methods : It tell the server what kind of action the client wants to perform.
# We can control which HTTP methods a route accepts — for forms or APIs.
'''
| Method     |             Use Case                  |
| ---------- | --------------------------------------|
| **GET**    | Retrieve data (default for browsers)  |
| **POST**   | Send data to the server (forms, APIs) |
| **PUT**    | Update data on the server             |
| **DELETE** | Delete data on the server             |
| **PATCH**  | Partial update                        |
'''

from flask import Flask, request

app = Flask(__name__)

# Server handles POST and returns data.
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"Hello {username}, Welcome to your profile. You are logged in!"
    
    # For GET request, show a simple form
    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit">
        </form>
    '''

if __name__ == '__main__':
    app.run(debug=True)
