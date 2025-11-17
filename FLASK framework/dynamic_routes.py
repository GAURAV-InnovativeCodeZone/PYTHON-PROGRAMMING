# URL Building (Dynamic Linking using url_for)

from flask import Flask, url_for
# url_for() : It is a Flask function used to build/generate URLs dynamically for a specific function name (routes-endpoints)

app = Flask(__name__)

@app.route('/about')
def about():
    return f"This is About Page! <a href='{url_for('srvce')}'>Go to Service Page</a>"   # use function_name inside url_for()

@app.route('/service')
def srvce():
    return "Now you are in the Service Page"

# Using url_for() to build a URL with parameter 'username'
@app.route('/')
def home():
    return "Go to your profile here: <a href='" + url_for('profile', username='Gaurav') + "'>Profile</a>"

@app.route('/user/<username>')
def profile(username):
    return f"Welcome to {username}'s Profile Page!"

# Works safely across blueprints, subdomains, and apps

@app.route('/product', endpoint='product_page')
def service():
    return "This is product page! Check my <a href='" + url_for('skill_page') + "'>Skill</a>"

@app.route('/skill', endpoint='skill_page')
def service():
    return "This is the Skills Page"

if __name__ == '__main__':
    app.run(debug=True)
