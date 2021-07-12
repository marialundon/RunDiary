from flask import Blueprint
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
app = Flask (__name__)
db = SQLAlchemy(app)

run_type_blueprint = Blueprint('run_type_blueprint', __name__, url_prefix="/type")

class Runtype(db.Model):
    __tablename__ = 'runtype'
    id = db.Column('runtype_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    

    def __init__(self, description):
        self.description = description

@run_type_blueprint.route('/')
def type_show_all():
    return render_template('type_show_all.html', Runtype = Runtype.query.all())