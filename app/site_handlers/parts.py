from flask import Blueprint, render_template, request, session
from app.utils.ProductHandler import ProductHandler

parts_bp = Blueprint("parts", __name__)

@parts_bp.route("/parts")
def parts():
    products = ProductHandler()
    return render_template("parts.html", products=products.get_products(), user_session=session["user"] if "user" in session else None)

@parts_bp.route("/parts", methods=["POST"])
def filter_parts():
    products = ProductHandler()
    filtered = []

    engine_code = request.form.get("engine-code")
    engine_main_part = request.form.get("engine-main-part")
    engine_part = request.form.get("engine-part")

    if engine_code == "nth" and engine_main_part == "nth" and engine_part == "nth":
        filtered = products.get_products()
    else:
        filtered = products.filter_products({"engine_code" : engine_code, "engine_main_part" : engine_main_part, "engine_part" : engine_part})
    
    return render_template("parts.html", products=filtered)
