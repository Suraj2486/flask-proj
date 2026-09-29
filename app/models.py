from app import db

class Menu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    price = db.Column(db.Float, nullable = False)

class User(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(200), nullable = False)
    email = db.Column(db.String(200), unique = True)

class Order(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable = False)

class OrderMenu(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    order_id = db.Column(db.Integer,db.ForeignKey('order.id'), nullable = False)
    menu_id = db.Column(db.Integer,db.ForeignKey('menu.id'), nullable = False)
    qauntity = db.Column(db.Integer, default = 1)