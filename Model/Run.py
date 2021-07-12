from flask.app import Flask
from Model import db

from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base


app = Flask('__main__')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"


db.init_app(app)
class Runs(db.Model):
    __tablename__ = 'runs'
    id = db.Column('run_id', db.Integer, primary_key = True)
    length = db.Column(db.String(50))
    location = db.Column(db.Integer, ForeignKey('runlocation.runlocation_id'))
    time = db.Column(db.String(10))
    typeofrun = db.Column(db.Integer, ForeignKey('runtype.runtype_id'))
    related_type_of_run = relationship('Runtype', backref='Runs',lazy="joined")
    related_location_of_run = relationship('Runlocation', backref='Runs',lazy="joined")

    def __init__(self, typeofrun, length, location, time):
        self.typeofrun = typeofrun
        self.length = length
        self.location = location
        self.time = time