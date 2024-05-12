from flask import Blueprint, render_template, request, session, redirect, url_for
from app.utils.ProductHandler import ProductHandler
from app.utils.CartHandler import CartHandler
from app.entity.CartItem import CartItem

product_bp = Blueprint("product", __name__)

@product_bp.route("/product", methods=["GET"])
def product():
    product = ProductHandler()
    part_id = request.args.get("part_id")
    p = product.find_product_by_id(part_id)

    if p == None:
        print(p)
        return redirect(url_for("parts.parts"))

    return render_template("product.html", product = p, reviews=product.get_reviews_for_product(part_id), user_session=session["user"] if "user" in session else None)


@product_bp.route("/placeProductToCart", methods=["POST"])
def placePorductToCart():
    products = ProductHandler()
    cart = CartHandler()

    product_id = int(request.form.get("id"))
    quantity = int(request.form.get("quantity"))

    selected_product = products.find_product_by_id(product_id)

    placeable_product = CartItem(selected_product, quantity)

    cart.add_item_to_cart(placeable_product)
    return "Termék sikeresen a kosárba helyezve!"

@product_bp.route("/addReview", methods=["POST"])
def addReview():

    star_rating = int(request.form.get("star-rating"))
    review_to_add = request.form.get("review-to-add")
    part_id = int(request.form.get("submit-review"))

    product = ProductHandler()

    product.add_review_for_product({
        "rating" : star_rating,
        "reviewText" : review_to_add,
        "part_id" : part_id,
        "reviewWriter" : session["user"]["felh_n"]
    })

    return redirect(url_for("product.product", part_id=part_id))