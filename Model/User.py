from flask.app import Flask
from Model import db
from flask_login import UserMixin

import json

app = Flask('__main__',template_folder = 'Templates')
import os
is_prod = os.environ.get('IS_HEROKU', None)

if is_prod:
    app.config ['SQLALCHEMY_DATABASE_URI'] = os.environ.get('SQLALCHEMY_DATABASE_URI', None)
    app.config ['SECRET_KEY'] = os.environ.get('SECRET_KEY', None)
else:
    with open('config.json', 'r') as f:
        config_data = json.load(f)

    app.config ['SQLALCHEMY_DATABASE_URI'] = config_data['SQLALCHEMY_DATABASE_URI']
    app.config ['SECRET_KEY'] = config_data['SECRET_KEY']


db.init_app(app)

class User(UserMixin,db.Model):
    __tablename__ = 'user'
    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(100), unique=True)
    password = db.Column(db.String(100))
    name = db.Column(db.String(1000))

def __init__(self, email, password, name):
    self.email = email
    self.password = password
    self.name = name