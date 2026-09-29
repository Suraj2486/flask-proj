from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from app import db
from app.models import Menu, Order, OrderMenu

order_bp = Blueprint('order', __name__)

@order_bp.route('/order', methods=["POST"])
def order():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user']
    
    new_order = Order(user_id=user_id)
    db.session.add(new_order)
    db.session.flush() 
    
    selected_item_ids = request.form.getlist('menu_items') 
    if not selected_item_ids:
        flash("Please select at least one item to order.", "error")
        return redirect(url_for('menu.view_item')) 
    for menu_id in selected_item_ids:
        qty = request.form.get(f'quantity_{menu_id}', 1) 
        order_item = OrderMenu(
            order_id=new_order.id, 
            menu_id=int(menu_id), 
            qauntity=int(qty)
        )
        db.session.add(order_item)
        
    db.session.commit()
    flash("Order placed successfully!", "success")
    return redirect(url_for('order.view_Allorder')) 


@order_bp.route('/view_allorder')
def view_Allorder():
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    user_id = session['user']
    orders = Order.query.filter_by(user_id=user_id).all()
    return render_template('view_allorder.html', orders=orders) 

@order_bp.route('/view_order/<int:order_id>') 
def view_order(order_id):
    if 'user' not in session:
        return redirect(url_for('auth.login'))
    order_items = OrderMenu.query.filter_by(order_id=order_id).all()
    return render_template('view_order.html', order=order_items)


