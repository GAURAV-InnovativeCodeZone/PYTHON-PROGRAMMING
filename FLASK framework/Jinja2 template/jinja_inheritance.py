from flask import Flask, render_template
from pathlib import Path

# Get the absolute path of the current file
BASE_DIR = Path(__file__).resolve().parent

# tell Flask where templates are located
app = Flask(__name__, template_folder=BASE_DIR / 'templates')

@app.route('/')
def home():
    return render_template("home.html", username = "Gaurav")

@app.route('/about')
def about():
    return render_template("about.html")

if __name__ == "__main__":
    app.run(debug=True)
