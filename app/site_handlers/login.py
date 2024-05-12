from flask import Blueprint, render_template, session, url_for, redirect, request
from app.utils.UsersHandler import UsersHandle
import re

login_bp = Blueprint("login", __name__)

@login_bp.route("/login")
def login():
    if "user" in session:
        return redirect(url_for("profile.profile"))

    return render_template("login.html", user_session=None)

@login_bp.route("/auth_user", methods=["POST"])
def auth_user():
    if "user" in session:
        pass
    
    uh = UsersHandle()
    u = uh.find_user(request.form["login__name"], request.form["login__password"])

    if u == None:
        return render_template("login.html", stat={"success": False, "msg": "Hibás jelszó vagy felhasználónév!"})

    #print("ok")
    session["user"] = u.to_dict()

    return redirect(url_for("index.index"))

@login_bp.route("/reg_user", methods=["POST"])
def reg_user():
    #print("reg")
    uh = UsersHandle()
    form_fields = ["reg__email", 
                   "reg__name", 
                   "reg__firstname", 
                   "reg__lastname", 
                   "reg__password", 
                   "reg__password__again", 
                   "reg__date", 
                   "reg__gender"]

    if  "reg__accept_terms" in request.form:
        for f in form_fields:
            if f not in request.form:
                return render_template("login.html", stat={"success": False, "msg": "Valamelyik űrlapmező nem lett kitöltve!"})
            
        reg_email = request.form.get("reg__email")
        reg_name = request.form.get("reg__name")
        reg_firstname = request.form.get("reg__firstname")
        reg_lastname = request.form.get("reg__lastname")
        reg_password = request.form.get("reg__password")
        reg_password_again = request.form.get("reg__password__again")
        reg_date = request.form.get("reg__date")
        reg_gender = request.form.get("reg__gender")    

        errors = []

        if len(reg_name.strip()) != 0 and len(reg_name) < 8:
            errors.append("A felhazsnálónévnek minimum 8 karakter hosszúnak kell lennie!") 
        elif not re.match(r'^[a-zA-Z0-9]*$', reg_name):
            errors.append("A felhasználónév tiltott karaktereket tartalmazz!")

        if len(reg_firstname.strip()) == 0 or len(reg_lastname.strip()) == 0:
            errors.append("A családi név vagy keresztnév kitöltése kötelező!")

        if len(reg_password.strip()) == 0 or len(reg_password_again.strip()) == 0:
            errors.append("A jelszó kitöltése kötelező!")
        elif reg_password != reg_password_again:
            errors.append("A két jelszó nem egyezik!") 

        if len(reg_email.strip()) != 0 and not re.match(r'^[a-zA-Z0-9._%+-]+@[a-zA-Z0-9.-]+\.[a-zA-Z]{2,}$', reg_email):
            errors.append("Nem megfelelő email cím formátum!")
        
        if len(errors) == 0:
            
            new_user = {
                "reg_name" : reg_name,
                "reg_firstname" : reg_firstname,
                "reg_lastname" : reg_lastname,
                "reg_password" : reg_password,
                "reg_email" : reg_email,
                "reg_gender" : reg_gender,
                "reg_date" : reg_date
            }
            
            res = uh.add_user(new_user)

            if res:
                return render_template("login.html", stat={"success": True, "msg": "Sikeres regisztráció!"})
            else:
                return render_template("login.html", stat={"success": False, "msg": "Ismeretlen hiba történt!"})  
        else :
            return render_template("login.html", stat={"success": False, "msg": "Hiba az űrlap mezők kitöltése közben!", "err": errors})

    else:
        return render_template("login.html", stat={"success": False, "msg": "Felhasználási feltételeket el kell fogadni!"})

    #return render_template("login.html", stat={"success": False, "msg": "Felhasználási feltételeket el kell fogadni!"})