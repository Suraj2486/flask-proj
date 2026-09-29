from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'Naina'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///temp.db'

    db.init_app(app)

    from app.models import Menu, User, Order, OrderMenu
    from app.routes.auth import auth_bp
    from app.routes.order import order_bp
    from app.routes.menu import menu_bp

    app.register_blueprint(auth_bp)
    app.register_blueprint(order_bp)
    app.register_blueprint(menu_bp) 
    return app