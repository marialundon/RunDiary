from flask.app import Flask
from Model import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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

class Shoe(db.Model):
    __tablename__ = 'shoes'
    id = db.Column('shoe_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    max_distance = db.Column(db.Integer)
    current_distance = db.Column(db.Integer)
    remaining_distance = db.Column(db.Integer)
    userid = db.Column(db.Integer,ForeignKey('user.id' ))

    def __init__(self, description,max_distance,userid):
        self.description = description
        self.max_distance = max_distance
        self.userid = userid