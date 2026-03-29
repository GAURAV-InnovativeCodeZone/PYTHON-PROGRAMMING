from flask import Flask, request, jsonify

app = Flask(__name__)

# -------------------------
# 1️⃣ Query parameters (GET)
# -------------------------
@app.route('/search')
def search():
    q = request.args.get('q')  # /search?q=flask
    return f"🔍 Searching for: {q}"


# -------------------------
# 2️⃣ Form data (POST)
# -------------------------
@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        return f"👤 Username: {username}, 🔑 Password: {password}"
    return '''
        <form method="POST">
            Username: <input type="text" name="username"><br>
            Password: <input type="password" name="password"><br>
            <input type="submit">
        </form>
    '''

# -------------------------
# 3️⃣ JSON data (POST)
# -------------------------
@app.route('/api/data', methods=['POST'])
def api_data():
    data = request.json
    return jsonify({
        "message": "✅ JSON received successfully",
        "your_data": data
    })


# -------------------------
# 4️⃣ Method used
# -------------------------
@app.route('/check', methods=['GET', 'POST'])
def check():
    return f"HTTP Method used: {request.method}"


# -------------------------
# 5️⃣ File upload
# -------------------------
@app.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'POST':
        file = request.files['myfile']

        # If user does not select a file
        if file.filename == '':
            return "⚠️ No file selected."

        # Save the file
        file.save(file.filename)
        return f"📁 File '{file.filename}' uploaded successfully!"

    # Show upload form on GET request
    return '''
        <form action="/upload" method="post" enctype="multipart/form-data">
            <input type="file" name="myfile" required><br><br>
            <button type="submit">Upload File</button>
        </form>
    '''


# -------------------------
# 6️⃣ Cookies
# -------------------------
@app.route('/cookie')
def cookie():
    username = request.cookies.get('username')
    return f"🍪 Cookie username: {username}"


# -------------------------
# 7️⃣ Headers
# -------------------------
@app.route('/headers')
def headers():
    user_agent = request.headers.get('User-Agent')
    return f"🧭 Your browser info: {user_agent}"


# -------------------------
# 8️⃣ URL details
# -------------------------
@app.route('/info')
def info():
    return f"🌐 Path: {request.path} <br> URL: {request.url}"


# -------------------------
# 9️⃣ Client IP
# -------------------------
@app.route('/ip')
def ip():
    return f"💻 Your IP address: {request.remote_addr}"


# -------------------------
# ✅ Home route (menu)
# -------------------------
@app.route('/')
def home():
    return '''
    <h2>Flask Request Demo</h2>
    <ul>
        <li><a href="/search?q=flask">/search?q=flask</a></li>
        <li><a href="/login">/login</a></li>
        <li><a href="/api_data">/api_data</a></li>
        <li><a href="/check">/check</a></li>
        <li><a href="/headers">/headers</a></li>
        <li><a href="/upload">/upload</a></li>
        <li><a href="/info">/info</a></li>
        <li><a href="/ip">/ip</a></li>
        <li><a href="/cookie">/cookie</a></li>
        <p>Use POST tools like Postman or HTML forms for /login, /api/data, /upload</p>
    </ul>
    '''


if __name__ == '__main__':
    app.run(debug=True)
