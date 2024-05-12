from flask import Blueprint, render_template, request, session
from app.utils.CartHandler import CartHandler

cart_bp = Blueprint("cart", __name__)

@cart_bp.route("/cart")
def cart():
    cart = CartHandler()
    print(len(cart.get_items_from_cart()))
    return render_template("cart.html", cartItems = cart.get_items_from_cart(), user_session=session["user"] if "user" in session else None)

