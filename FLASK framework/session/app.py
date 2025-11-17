'''
session : session is a Flask-provided dictionary-like object used to store information about a user between requests.
It uses secure cookies by default (client-side storage).
Each session is signed with a secret key to prevent tampering.
'''

from flask import Flask, render_template, request, redirect, url_for, session
from datetime import timedelta

app = Flask(__name__)
app.secret_key = "supersecretkey"

# Auto session timeout
app.permanent_session_lifetime = timedelta(seconds=10)


# -------------------------------------------------
# 1. APP OPENS DIRECTLY ON LOGIN PAGE
# -------------------------------------------------
@app.route("/")
def root():
    return redirect(url_for("login"))


# -------------------------------------------------
# 2. LOGIN PAGE + CREATE SESSION
# -------------------------------------------------
@app.route("/login", methods=["GET", "POST"])
def login():
    # IF ALREADY LOGGED IN
    if "user" in session:
        return redirect(url_for("index"))

    if request.method == "POST":
        username = request.form.get("username")
        if username:
            session.permanent = True
            session["user"] = username
            return redirect(url_for("index"))

    return render_template("login.html")
    

# -------------------------------------------------
# 3. MAIN PAGE (index.html)
#    - Show session active
# -------------------------------------------------
@app.route("/index")
def index():
    user = session.get("user")

    if not user:
        # Auto session expired → redirect with message
        return redirect(url_for("session_expired"))

    return render_template("index.html", user=user)


# -------------------------------------------------
# 4. MANUAL LOGOUT
# -------------------------------------------------
@app.route("/logout")
def logout():
    session.pop("user", None)
    return render_template("message.html",
                           title="Logged Out",
                           message="You are successfully logged out.",
                           link_text="Back to Login",
                           link_url=url_for("login"))


# -------------------------------------------------
# 5. SESSION EXPIRED HANDLER
# -------------------------------------------------
@app.route("/session_expired")
def session_expired():
    return render_template("message.html",
                           title="Session Expired",
                           message="Your session has expired. Please login again.",
                           link_text="Login Again",
                           link_url=url_for("login"))

user = session.get("user")
if user:
    print("User:", session["user"])  # Safe because we already checked

if __name__ == "__main__":
    app.run(debug=True)
