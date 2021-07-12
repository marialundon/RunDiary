from flask.templating import render_template
from Model.Run import Runs
from flask import Blueprint

show_run = Blueprint('show_run', __name__)

@show_run.route("/")
def run_show_all():
    return render_template('run_show_all.html', Runs = Runs.query.all())