"""Auth views module.
@todo #5:30min Implement before_app_request function that will get the user id
 from session, get user data from db and store it in g.user, which lasts for the
 length of the request. Also, create a decorator that will check, for each view
 if g.user exists and if not, redirect user to login page.
"""
from functools import wraps
from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from timeless.auth import auth
from timeless.employees.models import Employee

bp = Blueprint("auth", __name__, url_prefix="/auth")


@bp.before_app_request
def load_logged_in_user():
    user_id = session.get("user_id")
    if not user_id:
        g.user = None
    else:
        g.user = Employee.query.get(user_id)


def login_required(view):
    @wraps(view)
    def wrapped_view(**kwargs):
        if not g.user:
            return redirect(url_for("auth.login"))

        return view(**kwargs)

    return wrapped_view


@bp.route("/login", methods=("GET", "POST"))
def login():
    if request.method == "POST":
        error = auth.login(
            username=request.form["username"],
            password=request.form["password"])
        if error is not None:
            return redirect(url_for("auth.login"))

    return render_template("auth/login.html")


@bp.route("/logout")
def logout():
    session.clear()
    return redirect(url_for("main"))


@bp.route("/forgotpassword", methods=("GET", "POST"))
def forgot_password():
    if request.method == "POST":
        error = auth.forgot_password(email=request.form["email"])
        if error is not None:
            flash("We sent a password recover link to your email tst@mail.com")
            return redirect(url_for("auth.login"))
        else:
            flash("E-mail not found", "error")

    return render_template("auth/forgot_password.html")


@bp.route("/activate", methods=["POST"])
def activate():
    """ Activate the user's account by setting account status to true. """
    if g.user is None:
        return render_template("auth/activate.html")
    else:
        g.user.account_status = True
        session.commit()
        return render_template(
            "auth/activate.html",
            message="Successfully activated your account."
        )
