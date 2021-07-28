from flask import Blueprint
from Model import db
from flask import Blueprint, request, render_template, flash, url_for, redirect

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/logout')
def logout():
    return 'Logout'

@auth.route('/profile')
def profile():
    return render_template('profile.html')

@auth.route('/index')
def index():
    return render_template('index.html')