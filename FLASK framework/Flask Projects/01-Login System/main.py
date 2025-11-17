from flask import (
    Flask, render_template, request, redirect,
    url_for, flash, session
)
from datetime import datetime, timedelta
from functools import wraps

app = Flask(__name__)
app.secret_key = "your_secret_key"

# ---------------- FIXED USER ----------------
VALID_USERNAME = "admin"
VALID_PASSWORD = "1234"

# Remember-me lifetime
app.permanent_session_lifetime = timedelta(days=7)


# --------------- LOGIN REQUIRED DECORATOR ---------------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        if "user" not in session:
            flash("Please login first", "warning")
            return redirect(url_for("login"))
        return f(*args, **kwargs)
    return wrapper


# ----------------------- LOGIN -----------------------
@app.route("/", methods=["GET", "POST"])
def login():

    # Auto-logout due to session timeout
    if "last_active" in session:
        if datetime.now() > session["last_active"] + timedelta(minutes=1):
            session.clear()
            flash("Session expired, login again", "warning")
            return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        remember = request.form.get("remember")

        # Wrong password counter
        if "wrong_attempts" not in session:
            session["wrong_attempts"] = 0

        # Block after 3 wrong attempts
        if session["wrong_attempts"] >= 3:
            flash("Too many attempts. Try after 30 seconds.", "danger")
            return redirect(url_for("login"))

        if username == VALID_USERNAME and password == VALID_PASSWORD:

            # Successful login → reset attempts
            session["wrong_attempts"] = 0

            # Save user to session
            session["user"] = username

            # Remember me
            if remember:
                session.permanent = True
            else:
                session.permanent = False

            # Save last login time
            session["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

            # Default theme
            if "theme" not in session:
                session["theme"] = "light"

            # Update last active time
            session["last_active"] = datetime.now()

            flash("Login Successful!", "success")
            return redirect(url_for("dashboard"))

        else:
            session["wrong_attempts"] += 1
            flash(f"Invalid credentials. Attempts: {session['wrong_attempts']}/3",
                  "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


# ---------------------- DASHBOARD ----------------------
@app.route("/dashboard")
@login_required
def dashboard():
    session["last_active"] = datetime.now()  # Update activity
    return render_template(
        "dashboard.html",
        user=session["user"],
        last_login=session.get("last_login"),
        theme=session.get("theme", "light")
    )


# ---------------------- PROFILE PAGE ----------------------
@app.route("/profile")
@login_required
def profile():
    session["last_active"] = datetime.now()
    return render_template("profile.html",
                           user=session["user"],
                           theme=session.get("theme", "light"))


# ---------------------- CHANGE PASSWORD ----------------------
@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    global VALID_PASSWORD
    session["last_active"] = datetime.now()

    if request.method == "POST":
        old = request.form.get("old")
        new = request.form.get("new")

        if old != VALID_PASSWORD:
            flash("Old password is incorrect", "danger")
            return redirect(url_for("change_password"))

        VALID_PASSWORD = new
        flash("Password changed successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("change_password.html",
                           theme=session.get("theme", "light"))


# ---------------------- TOGGLE DARK MODE ----------------------
@app.route("/toggle-theme")
@login_required
def toggle_theme():
    session["theme"] = "dark" if session["theme"] == "light" else "light"
    flash(f"Theme changed to {session['theme']}", "info")
    return redirect(url_for("dashboard"))


# ---------------------- LOGOUT ----------------------
@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))


if __name__ == "__main__":
    app.run(debug=True)
