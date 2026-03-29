'''
Cookies are small pieces of data that the browser stores locally on your computer, which are sent back to the server on every request.
Cookies = client-side storage (saved in browser)
Session = server-side storage
'''

from flask import Flask, request, make_response

app = Flask(__name__)

# 
# Setting a cookie
@app.route('/set_cookie')
def set_cookie():
    resp = make_response("Cookie is set!")
    resp.set_cookie(
        'username',
        'gaurav',
        max_age=60*60*24*7  # expires in 7 days
    )
    return resp

# Reading a cookie
@app.route('/get_cookie')
def get_cookie():
    username = request.cookies.get('username')
    if username:
        return f'Cookie Value = {username}!'
    else:
        return 'No cookie found!'

# Deleting a cookie
@app.route('/delete_cookie')
def delete_cookie():
    resp = make_response("Cookie deleted!")
    resp.set_cookie('username', '', expires=0)
    return resp


if __name__ == "__main__":
    app.run(debug = True)