from flask import Flask
from flask_bootstrap import Bootstrap

from .config import Config
from .database import db


def init_app():
    app = Flask(__name__)
    bootstrap = Bootstrap(app)
    app.config.from_object(Config)  
    db.init_app(app)
    
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)
    
    from .category import category as category_blueprint
    app.register_blueprint(category_blueprint)
    
    from .product import product as product_blueprint
    app.register_blueprint(product_blueprint)
    
    return app
