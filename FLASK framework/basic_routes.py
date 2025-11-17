# BasicRouting in Flask allows you to map URLs to functions, enabling dynamic content delivery based on the requested path.

from flask import Flask

app = Flask(__name__)

# 1. Home route
@app.route('/')
def home():
    return "🏠 Welcome to the Home Page!"

# 2. About route
@app.route('/about')
def about():
    return "ℹ️ This is the About Page."

# 3. Contact route
@app.route('/contact')
def contact():
    return "📞 Contact us at example@gmail.com"

# 4. Dynamic route with parameter
@app.route('/user/<username>')
def user(username):
    return f"Hello, {username}! 👋"

# 5. Route with integer parameter
@app.route('/square/<int:number>')
def square(number):
    return f"The square of {number} is {number ** 2}"

if __name__ == '__main__':
    app.run(debug=True)


