'''
flash() : It's allow to store a short message in the session and display it once (on next page load), then remove it automatically.
It's showing temporary messages (like “Login Successful”, “Error occurred”, “Item added to cart”).
It's essential for user feedback, forms, and authentication systems.
'''

from flask import Flask, flash, redirect, render_template, url_for

app = Flask(__name__)
# Required for flash() to work & Required for session security
app.secret_key = "mysecretkey"

# flash(message) : Store message temporarily like - flash("Done!")
@app.route('/')
def home():
    return render_template('home.html', username = "Gaurav")

# flash(message, category) : Add message type like - flash("Done!", "success")
@app.route('/login')
def login():
    flash("✅ You are now logged in!", "success")
    return redirect(url_for('home'))

@app.route('/logout')
def logout():
    flash("👋 You are now logged out.", "info")
    return redirect(url_for('home'))

@app.route('/error')
def error():
    flash("❌ Something went wrong!", "danger")
    return redirect(url_for('home'))

@app.route('/permission')
def permission():
    flash("🚫 Access denied!", "warning")
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)
    
    