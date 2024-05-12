from flask import Blueprint, render_template, session

wiki_bp = Blueprint("wiki", __name__)

@wiki_bp.route("/wiki")
def wiki():
    return render_template("wiki.html", user_session=session["user"] if "user" in session else None)