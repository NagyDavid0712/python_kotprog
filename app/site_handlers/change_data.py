from flask import Blueprint, redirect, request, session, render_template, url_for
from app.utils.UsersHandler import UsersHandle

change_data_bp = Blueprint("change_data", __name__)

@change_data_bp.route("/change_data")
def change_data():
    if "user" not in session:
        return redirect(url_for("index.index"))
    return render_template("change_data.html", user_session=session["user"])

""""
@change_data_bp.route("/change_profile_pic", methods=["POST"])
def change_profile_pic():
    if "new_prof_pic" not in request.files:
        return redirect(url_for("change_data.change_data"))
    
    new_prof_pic = request.files["new_prof_pic"]

    if new_prof_pic.filename == "":
        return redirect(url_for("change_data.change_data"))
    
    uh = UsersHandle()
    uh.update_prof_pic(new_prof_pic)

    redirect(url_for("profile.profile"))
"""

@change_data_bp.route("/change_password", methods=["POST"])
def change_password():
    password = request.form.get("new_password")
    password_again = request.form.get("new_password_again")
    if len(password.strip()) == 0 or len(password_again.strip()) == 0:
        return render_template("change_data.html", user_session=session["user"], msg="Valamelyik mező nincs kitöltve!")

    if password != password_again:
        return render_template("change_data.html", user_session=session["user"], msg="A két jelszó nem egyezik!")

    uh = UsersHandle()

    if uh.update_password(password, session["user"]["felh_n"]):
        return render_template("change_data.html", user_session=session["user"], msg="Jelszó változtatás sikeres!")
    
    return render_template("change_data.html", user_session=session["user"], msg="Ismeretlen hiba történt!")
