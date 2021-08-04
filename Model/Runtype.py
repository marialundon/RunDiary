from flask.app import Flask
from Model import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

import json

app = Flask('__main__')
with open('config.json', 'r') as f:
	config_data = json.load(f)

app.config ['SQLALCHEMY_DATABASE_URI'] = config_data['SQLALCHEMY_DATABASE_URI']
app.config ['SECRET_KEY'] = config_data['SECRET_KEY']


db.init_app(app)

class Runtype(db.Model):
    __tablename__ = 'runtype'
    id = db.Column('runtype_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    userid = db.Column(db.Integer,ForeignKey('user.id' ))
    

    def __init__(self, description,userid):
        self.description = description
        self.userid = userid