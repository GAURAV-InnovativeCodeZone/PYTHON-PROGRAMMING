"""
Middleware in Flask is a function that runs before or after every request.
It's useful for logging, authentication, modifying requests, etc.
"""

# Example: Logging middleware

from flask import Flask, request

app = Flask(__name__)


# runs before each request
@app.before_request
def before_request_logging():
    print(f"Incoming request: {request.method} {request.path}")


# runs after each request
@app.after_request
def after_request_logging(response):
    app.logger.info(f"Response status: {response.status}")
    return response


if __name__ == "__main__":
    app.run(debug=True)
