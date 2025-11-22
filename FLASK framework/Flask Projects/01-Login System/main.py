from flask import (
    Flask,
    render_template,
    request,
    redirect,
    url_for,
    flash,
    session,
    jsonify,
)
from functools import wraps
from datetime import datetime, timedelta
import json
import os
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
app.secret_key = "my_secret_key"

# session permanent lifetime used for "remember me"
app.permanent_session_lifetime = timedelta(days=7)

USERS_FILE = "users.json"
INACTIVITY_LIMIT = timedelta(minutes=1)  # auto-logout after 1 minute inactivity
BLOCK_SECONDS = 30  # block 30 seconds after 3 wrong attempts
MAX_WRONG = 3


# ---------- Helpers: load/save users ----------
def load_users():
    if not os.path.exists(USERS_FILE):
        with open(USERS_FILE, "w") as f:
            json.dump({}, f)
        return {}
    with open(USERS_FILE, "r") as f:
        try:
            return json.load(f)
        except json.JSONDecodeError:
            return {}


def save_users(users):
    with open(USERS_FILE, "w") as f:
        json.dump(users, f, indent=2)


# ---------- Context processor (provide theme & current_user to templates) ----------
@app.context_processor
def inject_user_theme():
    return {"theme": session.get("theme", "light"), "current_user": session.get("user")}


# ---------- Login required decorator ----------
def login_required(f):
    @wraps(f)
    def wrapper(*args, **kwargs):
        # auto-logout check
        last_active_ts = session.get("last_active")
        if last_active_ts:
            last_active = datetime.fromtimestamp(last_active_ts)
            if datetime.now() - last_active > INACTIVITY_LIMIT:
                session.clear()
                flash("Session expired, login again", "warning")
                return redirect(url_for("login"))

        if "user" not in session:
            flash("Please login first", "warning")
            return redirect(url_for("login"))
        # update last_active
        session["last_active"] = datetime.now().timestamp()
        return f(*args, **kwargs)

    return wrapper


# ---------- Routes ----------
@app.route("/", methods=["GET", "POST"])
def login():
    users = load_users()

    # initialize wrong_attempts and blocked_until in session if not present
    if "wrong_attempts" not in session:
        session["wrong_attempts"] = {}  # dict: username -> int
    if "blocked_until" not in session:
        session["blocked_until"] = {}  # dict: username -> timestamp

    # auto-logout due inactivity BEFORE showing login page
    last_active_ts = session.get("last_active")
    if last_active_ts:
        last_active = datetime.fromtimestamp(last_active_ts)
        if datetime.now() - last_active > INACTIVITY_LIMIT:
            session.clear()
            flash("Session expired, login again", "warning")
            return redirect(url_for("login"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        remember = request.form.get("remember")

        if not username or not password:
            flash("Enter username and password", "danger")
            return redirect(url_for("login"))

        # check blocked status
        blocked_until_ts = session["blocked_until"].get(username)
        if blocked_until_ts:
            if datetime.now().timestamp() < blocked_until_ts:
                remaining = int(blocked_until_ts - datetime.now().timestamp())
                flash(f"Too many attempts. Try after {remaining} seconds.", "danger")
                return redirect(url_for("login"))
            else:
                # unblock after time passed
                session["blocked_until"].pop(username, None)
                session["wrong_attempts"].pop(username, None)

        user = users.get(username)
        if not user:
            flash("No such user. Please register first.", "danger")
            return redirect(url_for("login"))

        # verify password
        if check_password_hash(user["password_hash"], password):
            # success: reset counters
            session["wrong_attempts"].pop(username, None)
            session["blocked_until"].pop(username, None)

            # set session user
            session["user"] = username
            session["last_login"] = user.get("last_login")  # previous last_login
            # update last_login in users file to now
            users[username]["last_login"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            save_users(users)

            # remember me
            if remember:
                session.permanent = True
            else:
                session.permanent = False

            # default theme if not present
            if "theme" not in session:
                session["theme"] = "light"

            session["last_active"] = datetime.now().timestamp()
            flash("Login Successful!", "success")
            return redirect(url_for("dashboard"))
        else:
            # wrong password handling
            cur = session["wrong_attempts"].get(username, 0) + 1
            session["wrong_attempts"][username] = cur
            if cur >= MAX_WRONG:
                # block for BLOCK_SECONDS
                session["blocked_until"][username] = (
                    datetime.now() + timedelta(seconds=BLOCK_SECONDS)
                ).timestamp()
                flash(
                    f"Too many attempts. Blocked for {BLOCK_SECONDS} seconds.", "danger"
                )
            else:
                flash(f"Invalid credentials. Attempts: {cur}/{MAX_WRONG}", "danger")
            return redirect(url_for("login"))

    return render_template("login.html")


@app.route("/register", methods=["GET", "POST"])
def register():
    users = load_users()
    if request.method == "POST":
        username = request.form.get("username", "").strip()
        password = request.form.get("password", "")
        confirm = request.form.get("confirm", "")

        if not username or not password:
            flash("Fill all fields", "danger")
            return redirect(url_for("register"))
        if password != confirm:
            flash("Passwords do not match", "danger")
            return redirect(url_for("register"))
        if username in users:
            flash("Username already exists", "danger")
            return redirect(url_for("register"))

        users[username] = {
            "password_hash": generate_password_hash(password),
            "last_login": None,
            "bio": f"This is {username}'s profile bio.",
        }
        save_users(users)
        flash("Registration successful. Please login.", "success")
        return redirect(url_for("login"))

    return render_template("register.html")


@app.route("/dashboard")
@login_required
def dashboard():
    username = session["user"]
    users = load_users()
    user = users.get(username, {})
    # last_login shown is previous login stored in users file
    last_login = session.get("last_login") or user.get("last_login")
    return render_template("dashboard.html", user=username, last_login=last_login)


@app.route("/profile")
@login_required
def profile():
    username = session["user"]
    users = load_users()
    user = users.get(username, {})
    bio = user.get("bio", "")
    return render_template("profile.html", user=username, bio=bio)


@app.route("/change-password", methods=["GET", "POST"])
@login_required
def change_password():
    username = session["user"]
    users = load_users()
    user = users.get(username)

    if request.method == "POST":
        old = request.form.get("old", "")
        new = request.form.get("new", "")
        confirm = request.form.get("confirm", "")

        if not old or not new:
            flash("Fill all fields", "danger")
            return redirect(url_for("change_password"))
        if new != confirm:
            flash("New passwords do not match", "danger")
            return redirect(url_for("change_password"))

        if not check_password_hash(user["password_hash"], old):
            flash("Old password is incorrect", "danger")
            return redirect(url_for("change_password"))

        users[username]["password_hash"] = generate_password_hash(new)
        save_users(users)
        flash("Password changed successfully!", "success")
        return redirect(url_for("dashboard"))

    return render_template("change_password.html")


@app.route("/toggle-theme")
@login_required
def toggle_theme():
    session["theme"] = "dark" if session.get("theme", "light") == "light" else "light"
    flash(f"Theme changed to {session['theme']}", "info")
    return redirect(url_for("dashboard"))


@app.route("/logout")
def logout():
    session.clear()
    flash("Logged out successfully!", "info")
    return redirect(url_for("login"))


# optional: endpoint to see session (for debugging only — remove in prod)
@app.route("/_debug/session")
def debug_session():
    return jsonify({k: str(v) for k, v in session.items()})


if __name__ == "__main__":
    app.run(debug=True)
