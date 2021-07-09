from flask import Blueprint

show_run = Blueprint('show_run', __name__)

@show_run.route("/")
def show_runList():
    return "list of accounts"