''' Decorators can add functionality to routes without changing the route logic.'''

from flask import Flask, request
import time
from functools import wraps

app = Flask(__name__)

#Example: Timing requests
def timer(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        print(f"Execution time: {end-start:.4f}s")
        return result
    return wrapper

@app.route('/slow')
@timer
def slow():
    time.sleep(2)
    return "Finished after 2 seconds!"

if __name__ == '__main__':
    app.run(debug=True)