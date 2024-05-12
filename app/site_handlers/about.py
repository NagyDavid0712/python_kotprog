from flask import Blueprint, render_template, session

about_bp = Blueprint("about", __name__)

@about_bp.route("/about")
def about():
    #instance = ProductHandler.ProductHandler()
    #instance.read_products()

    return render_template("about.html", user_session=session["user"] if "user" in session else None)