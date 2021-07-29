# pylint: disable=no-member 

from flask_login import LoginManager
from Controllers.RunController import options_run,new_run, data_run, update_run, delete_run
from Controllers.RuntypeController import options_type,new_type, data_type, update_type, delete_type
from Controllers.ShoeController import options_shoe,new_shoe, data_shoe, update_shoe, delete_shoe
from Controllers.RunlocationController import options_location,new_location, data_location, update_location, delete_location
from Controllers.AuthController import auth
from flask import Flask, Blueprint
from flask import Blueprint, request, render_template, url_for, redirect, flash
from flask_login import current_user
from Model import db

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"
db.init_app(app)

main = Blueprint('main', __name__)



app.register_blueprint(options_run)

app.register_blueprint(new_run)

app.register_blueprint(data_run)

app.register_blueprint(update_run)

app.register_blueprint(delete_run)

app.register_blueprint(options_type)

app.register_blueprint(new_type)

app.register_blueprint(data_type)

app.register_blueprint(update_type)

app.register_blueprint(delete_type)

app.register_blueprint(options_shoe)

app.register_blueprint(new_shoe)

app.register_blueprint(data_shoe)

app.register_blueprint(update_shoe)

app.register_blueprint(delete_shoe)

app.register_blueprint(options_location)

app.register_blueprint(new_location)

app.register_blueprint(data_location)

app.register_blueprint(update_location)

app.register_blueprint(delete_location)

app.register_blueprint(auth)

app.register_blueprint(main)




login_manager = LoginManager()
login_manager.login_view = 'auth.login'
login_manager.init_app(app)

from Model.User import User

@login_manager.user_loader
def load_user(user_id):
    # since the user_id is just the primary key of our user table, use it in the query for the user
    return User.query.get(int(user_id))

@main.route('/profile')
def profile():
    return render_template('profile.html',name = current_user.name)

@main.route('/index')
def index():
    return render_template('index.html')

if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
