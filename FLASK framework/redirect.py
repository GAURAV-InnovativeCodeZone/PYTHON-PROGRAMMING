from flask import Flask, redirect, url_for
# redirect() : It is used to send/move the user from one route (URL) to another.

app = Flask(__name__)

# Basic Redirecting or without url_for()
@app.route('/')
def home():
    return "🏠 Welcome to Home Page"

@app.route('/go_to_about')
def go_to_about():
    return redirect('/about')

@app.route('/about')
def about():
    return "ℹ️ This is About Page"


# Redirect with url_for() : Use url_for() with the function name instead Hardcoding URLs (like '/routes') can break if you rename routes.
# (Best Practice)
@app.route('/go_home')
def go_home():
    return redirect(url_for('login'))


# Redirect with Parameters : We can pass parameters inside url_for().
@app.route('/user/<name>')
def user_profile(name):
    return f"👤 Hello, {name}!"

@app.route('/login_success')
def login_success():
    username = "Gaurav"
    return redirect(url_for('user_profile', name=username))


# Redirect with HTTP Status Code : By default Flask sends 302 (Temporary Redirect) but we can customize it.
@app.route('/status_code')
def status_code():
    return redirect(url_for('home'), code=301)  # Permanent redirect


# Login Redirect Example
@app.route('/login')
def login():
    user_logged_in = True  # Assume successful login
    if user_logged_in:
        return redirect(url_for('dashboard'))
    return "❌ Login failed"

@app.route('/dashboard')
def dashboard():
    return "✅ Welcome to your Dashboard"
if __name__ == '__main__':
    app.run(debug=True)