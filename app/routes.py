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
            if check_user.check_password(password):
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

        from .utils.validation import length_check, complexity_check

        if not length_check(password, 8) or not complexity_check(password, True, True, True, True):
            flash("Password is not secure","warning")
            return render_template("register.html")

        new_user = User(email=email)
        new_user.set_password(password)
        db.session.add(new_user)
        db.session.commit()

        flash("Registration successful", "success")
        return redirect(url_for("main.home"))

    return render_template("register.html")

@main.route("/products")
def products():
    from .models import Product
    products = Product.query.all()
    return render_template("products.html",products=products)