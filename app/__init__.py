from flask import Flask
from app.site_handlers.index import index_bp
from app.site_handlers.about import about_bp
from app.site_handlers.cart import cart_bp
from app.site_handlers.wiki import wiki_bp
from app.site_handlers.login import login_bp
from app.site_handlers.parts import parts_bp
from app.site_handlers.product import product_bp
from app.site_handlers.profile import profile_bp
from app.site_handlers.change_data import change_data_bp

def create_app():
    app = Flask(__name__, static_folder="../static", template_folder="../pages")
    app.config["SECRET_KEY"] = "szupertitkoskulcs"
    app.config["UPLOAD_FOLDER"] =  "../static/img/user"
    app.register_blueprint(index_bp)
    app.register_blueprint(about_bp)
    app.register_blueprint(cart_bp)
    app.register_blueprint(wiki_bp)
    app.register_blueprint(login_bp)
    app.register_blueprint(parts_bp)
    app.register_blueprint(product_bp)
    app.register_blueprint(profile_bp)
    app.register_blueprint(change_data_bp)
    return app