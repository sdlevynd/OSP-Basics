from flask import Blueprint, render_template, request, flash, redirect, url_for

main = Blueprint("main", __name__)

@main.route('/')
def home():  # put application's code here
    return render_template("home.html")

@main.route('/login', methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        from .models import User
        from app import db
        check_user = User.query.filter_by(email=email).first()
        if not check_user:
            flash("Email not found", "error")
            return render_template("login.html")
        else:
            if password == check_user.password:
                flash("Login successful", "success")
                return redirect(url_for("main.home"))
            else:
                flash("Login unsuccessful", "error")
                return render_template("login.html")

    return render_template("login.html")

@main.route('/register', methods=["GET", "POST"])
def register():  # put application's code here
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        from .models import User
        from app import db

        check_user = User.query.filter_by(email=email).first()
        if check_user:
            flash("Email already in use", "warning")
            return render_template("register.html")

        new_user = User(email=email, password=password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful", "success")
        return redirect(url_for("main.home"))

    return render_template("register.html")