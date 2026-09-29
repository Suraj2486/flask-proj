from flask import Blueprint, render_template, redirect, request, url_for, flash, session
from app import db
from app.models import User

auth_bp = Blueprint('auth', __name__)

@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if request.method == 'POST':
        name = request.form.get("name")
        email = request.form.get('email')
        existing_user = User.query.filter_by(email=email).first()
        if existing_user:
            flash("Email address already registered. Please login instead.", 'error')
            return render_template('register.html')
            
        if name and email:
            new_user = User(name=name, email=email)
            db.session.add(new_user)
            db.session.commit()
            flash("Registered successfully", 'success')
            return redirect(url_for('auth.login'))
        else:
            flash("Registration failed. Please fill out all fields.", 'error')
    return render_template('register.html')


@auth_bp.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        email = request.form.get("email")
        if email == 'admin':
            session['admin'] = 'admin'
            return redirect(url_for("menu.view_item"))
        user = User.query.filter_by(email=email).first()
        if user:
            session["user"] = user.id
            flash("Logged in successfully", 'success')
            return redirect(url_for('menu.view_item')) 
        else:
            flash("Invalid email reference occurred", 'error')
            
    return render_template('login.html') 


@auth_bp.route('/logout')
def logout():
    session.pop('user', None)
    session.pop('admin', None)
    flash('Logged out', 'info')
    return redirect(url_for('auth.login'))
