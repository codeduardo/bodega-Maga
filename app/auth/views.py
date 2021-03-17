from flask import render_template

from . import auth

@auth.route('/login')
def login():
    return render_template('auth/login.html')

# @auth.route('/login-post', methods=['POST']):
# def login_post()