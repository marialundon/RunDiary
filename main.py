from flask import Flask, render_template 
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'

db = SQLAlchemy(app)
class runs(db.Model):
   id = db.Column('run_id', db.Integer, primary_key = True)
   typeofrun = db.Column(db.String(100))
   length = db.Column(db.String(50))  
   location = db.Column(db.String(200))
   time = db.Column(db.String(10))

def __init__(self, typeofrun, length, location,time):
   self.typeofrun = typeofrun
   self.length = length
   self.location = location
   self.time = time

db.create_all()