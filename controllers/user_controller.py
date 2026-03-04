from flask import Blueprint, render_template, request, redirect, url_for, session
from models.user_model import UserModel

user_bp = Blueprint('user', __name__)

@user_bp.route("/")
def home():
    return render_template("index.html")

@user_bp.route("/about")
def about():
    return render_template("about.html")

@user_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == "POST":
        UserModel.register(
            request.form["name"],
            request.form["email"],
            request.form["password"]
        )
        return redirect(url_for("user.login"))

    return render_template("register.html")

@user_bp.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        user = UserModel.login(
            request.form["email"],
            request.form["password"]
        )

        if user:
            session["user_id"] = user[0]
            return redirect(url_for("user.select_role"))

        return redirect(url_for("user.login"))

    return render_template("login.html")

@user_bp.route("/select_role", methods=["GET", "POST"])
def select_role():
    if request.method == "POST":
        role = request.form["role"]
        UserModel.update_role(session["user_id"], role)

        if role == "servicer":
            return redirect(url_for("servicer.dashboard"))
        else:
            return redirect(url_for("booking.customer_dashboard"))

    return render_template("select_role.html")

@user_bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("user.home"))