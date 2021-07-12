# pylint: disable=no-member 

from Controllers.RunController import show_run,new_run, data_run, update_run, delete_run
from Controllers.RuntypeController import show_type,new_type, data_type, update_type, delete_type
from Controllers.RunlocationController import show_location,new_location, data_location, update_location, delete_location
from Model.Run import Runs
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Table, Column, Integer, ForeignKey
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base
from Model import db

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"
db.init_app(app)

app.register_blueprint(show_run)

app.register_blueprint(new_run)

app.register_blueprint(data_run)

app.register_blueprint(update_run)

app.register_blueprint(delete_run)

app.register_blueprint(show_type)

app.register_blueprint(new_type)

app.register_blueprint(data_type)

app.register_blueprint(update_type)

app.register_blueprint(delete_type)

app.register_blueprint(show_location)

app.register_blueprint(new_location)

app.register_blueprint(data_location)

app.register_blueprint(update_location)

app.register_blueprint(delete_location)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
