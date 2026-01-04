from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
import sqlite3

app = Flask(__name__)
app.secret_key = "secretkey123"

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# ---------------- DATABASE ----------------
def get_db():
    return sqlite3.connect("employees.db")

def init_db():
    with get_db() as db:
        db.execute("""CREATE TABLE IF NOT EXISTS admin (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT
        )""")

        db.execute("""CREATE TABLE IF NOT EXISTS employee (
            id INTEGER PRIMARY KEY,
            name TEXT,
            email TEXT,
            position TEXT,
            salary INTEGER
        )""")

        admin = db.execute("SELECT * FROM admin").fetchone()
        if not admin:
            db.execute("INSERT INTO admin VALUES (1, 'admin', ?)",
                       (generate_password_hash("admin123"),))

init_db()

# ---------------- AUTH ----------------
class Admin(UserMixin):
    def __init__(self, id):
        self.id = id

@login_manager.user_loader
def load_user(user_id):
    return Admin(user_id)

@app.route("/", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = request.form["username"]
        pwd = request.form["password"]

        db = get_db()
        admin = db.execute("SELECT * FROM admin WHERE username=?", (user,)).fetchone()

        if admin and check_password_hash(admin[2], pwd):
            login_user(Admin(admin[0]))
            return redirect("/dashboard")
        flash("Invalid Credentials")
    return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect("/")

# ---------------- DASHBOARD ----------------
@app.route("/dashboard")
@login_required
def dashboard():
    db = get_db()
    employees = db.execute("SELECT * FROM employee").fetchall()
    return render_template("dashboard.html", employees=employees)

# ---------------- CRUD ----------------
@app.route("/add", methods=["GET", "POST"])
@login_required
def add():
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        position = request.form["position"]
        salary = request.form["salary"]

        if not name or not email:
            flash("All fields required")
            return redirect("/add")

        db = get_db()
        db.execute("INSERT INTO employee (name,email,position,salary) VALUES (?,?,?,?)",
                   (name, email, position, salary))
        db.commit()
        return redirect("/dashboard")
    return render_template("add_employee.html")

@app.route("/edit/<int:id>", methods=["GET", "POST"])
@login_required
def edit(id):
    db = get_db()
    emp = db.execute("SELECT * FROM employee WHERE id=?", (id,)).fetchone()

    if request.method == "POST":
        db.execute("""UPDATE employee SET 
            name=?, email=?, position=?, salary=? WHERE id=?""",
            (request.form["name"], request.form["email"],
             request.form["position"], request.form["salary"], id))
        db.commit()
        return redirect("/dashboard")

    return render_template("edit_employee.html", emp=emp)

@app.route("/delete/<int:id>")
@login_required
def delete(id):
    db = get_db()
    db.execute("DELETE FROM employee WHERE id=?", (id,))
    db.commit()
    return redirect("/dashboard")

if __name__ == "__main__":
    app.run(debug=True)
