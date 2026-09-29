from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from app import db
from app.models import Menu

menu_bp = Blueprint("menu", __name__)

@menu_bp.route('/view', methods=['GET'])
def view_item():
    items = Menu.query.all()
    if 'admin' in session:
        return render_template('admin.html', items=items)
    return render_template('home.html', items=items)

@menu_bp.route('/add_item', methods=['POST'])
def add_item():
    if 'admin' not in session:
        return redirect(url_for('auth.login'))
    name = request.form.get('name')
    price = request.form.get('price')
    if name and price:
        new_item = Menu(name=name, price=float(price))
        db.session.add(new_item) 
        db.session.commit()   
        flash("Item added successfully", 'success')
    return redirect(url_for('menu.view_item'))

@menu_bp.route('/delete_item/<int:item_id>', methods=['POST']) 
def delete_item(item_id):
    if 'admin' not in session:
        return redirect(url_for('auth.login'))
    item = Menu.query.filter_by(id=item_id).first()
    if item:
        db.session.delete(item)
        db.session.commit()
        flash('Item deleted successfully', 'success')
    else:
        flash('Item not found', 'error')
    return redirect(url_for("menu.view_item"))
