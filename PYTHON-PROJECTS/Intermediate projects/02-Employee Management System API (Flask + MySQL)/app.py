from flask import Flask, render_template
from routes.employee_routes import employee_bp
from flasgger import Swagger

app = Flask(__name__)
Swagger(app)

app.register_blueprint(employee_bp)

@app.route('/')
def home():
    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
