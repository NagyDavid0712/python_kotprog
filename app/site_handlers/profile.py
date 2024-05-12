from flask import Blueprint, render_template, session, url_for, redirect
from app.utils.UsersHandler import UsersHandle

profile_bp = Blueprint("profile", __name__)

@profile_bp.route("/profile")
def profile():
    if "user" not in session:
        return redirect(url_for("login.login"))
    uh = UsersHandle()
    return render_template("profile.html", user_session=session["user"], reviews=uh.get_user_reviews(session["user"]["felh_n"]))

@profile_bp.route("/logout")
def logout():
    session.pop("user", None)
    return redirect(url_for("index.index"))