from flask import render_template,redirect, url_for,flash
from flask_login import login_user,logout_user

from ..forms import LoginForm
from ..database import Usuario
from . import auth

@auth.route('/login',methods = ['GET', 'POST'])
def login():
    login_form = LoginForm()
    
    if login_form.validate_on_submit():
        user  = Usuario.query.filter_by(username = login_form.username.data).first()
        if user :
            if user.check_password(login_form.password.data):
                login_user(user)
                return redirect(url_for('category.home'))
    
    return render_template('auth/login.html',login_form = login_form)

@auth.route('/logout')
def logout():
    logout_user()
    flash('Sesión Cerrada', category='success')
    return redirect(url_for('auth.login'))