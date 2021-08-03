from flask.app import Flask
from Model import db

from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship



app = Flask('__main__')
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"


db.init_app(app)

class Shoe(db.Model):
    __tablename__ = 'shoes'
    id = db.Column('shoe_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    userid = db.Column(db.Integer,ForeignKey('user.id' ))

    def __init__(self, description, userid):
        self.description = description
        self.userid = userid