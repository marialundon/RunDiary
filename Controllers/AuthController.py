from operator import mod
from flask import Blueprint
from Model import db
from flask import Blueprint, request, render_template, url_for, redirect, flash, Markup
from werkzeug.security import generate_password_hash, check_password_hash
from Model.User import User
from flask_login import login_user
from flask_login import current_user
from flask_login import login_user, logout_user, login_required
from pathlib import Path
auth = Blueprint('auth', __name__)

@auth.route('/')
def login():
    mod_path = Path(__file__).parent
    src_path_1 = (mod_path / 'login.html').resolve()
    return render_template(src_path_1.name)

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).first()

    if user: 
        flash('Email address already exists')
        return redirect(url_for('auth.signup'))

    new_user = User(email=email, name=name, password = generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    flash(Markup('''<div class="alert alert-success alert-dismissible">
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
            <strong>Account successfully created, </strong> Please log in to continue
          </div>'''))
    return redirect(url_for('auth.login'))

@auth.route('/login', methods=['POST'])
def login_post():
    email = request.form.get('email')
    password = request.form.get('password')
    remember = True if request.form.get('remember') else False

    user = User.query.filter_by(email=email).first()

    if not user or not check_password_hash(user.password, password):
        flash(Markup('''<div class="alert alert-danger alert-dismissible">
            <a href="#" class="close" data-dismiss="alert" aria-label="close">&times;</a>
            <strong>Incorrect Username or Password,</strong> Please try again
          </div>'''))
        return redirect(url_for('auth.login'))

    login_user(user, remember=remember)
    return redirect(url_for('options_run.run_options'))

@auth.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('auth.login'))

