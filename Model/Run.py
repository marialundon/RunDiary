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
class Run(db.Model):
    __tablename__ = 'runs'
    id = db.Column('run_id', db.Integer, primary_key = True)
    length = db.Column(db.String(50))
    location = db.Column(db.Integer, ForeignKey('runlocation.runlocation_id'))
    time = db.Column(db.String(10))
    shoe = db.Column(db.Integer, ForeignKey('shoes.shoe_id'))
    userid = db.Column(db.Integer,ForeignKey('user.id' ))
    date = db.Column(db.String(10))
    typeofrun = db.Column(db.Integer, ForeignKey('runtype.runtype_id'))
    related_type_of_run = relationship('Runtype', backref='Run',lazy="joined")
    related_location_of_run = relationship('Runlocation', backref='Run',lazy="joined")
    related_shoe_of_run = relationship('Shoe', backref='Run',lazy="joined")

    def __init__(self, typeofrun, date, length, time, location, shoe, userid):
        self.typeofrun = typeofrun
        self.date = date
        self.length = length
        self.time = time
        self.shoe = shoe
        self.location = location
        self.userid = userid