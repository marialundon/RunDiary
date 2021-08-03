from flask.app import Flask
from Model import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship


app = Flask('__main__')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"


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