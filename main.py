# pylint: disable=no-member 

from Controllers.RunController import show_run,new_run, data_run, update_run, delete_run
from Controllers.RuntypeController import show_type,new_type, data_type, update_type, delete_type
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






@app.route('/location')
def location_show_all():
    return render_template('location_show_all.html', Runlocation = Runlocation.query.all())

@app.route('/location/locationdata')
def location_data():
    runlocation = Runlocation.query.all()
    return render_template('location_data.html',data = runlocation)

@app.route('/location/locationnew', methods = ['GET', 'POST'])
def location_new():
    if request.method == 'POST':
        if not request.form.get('runlocation',''):
            flash('Please enter all the fields', 'error')
        else:
            runlocation = Runlocation(request.form.get('runlocation',''))
            db.session.add(runlocation)
            db.session.commit()
            flash('Run type was successfully added')
            return redirect(url_for('location_show_all'))
    return render_template('location_new.html')

@app.route('/location/locationdelete/<id>', methods=['POST','DELETE','GET'])
def location_delete(id):
    runlocation = Runlocation.query.get_or_404(id)
    db.session.delete(runlocation)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('location_show_all'))

@app.route('/location/locationupdate/<id>', methods=["GET","POST"])
def location_update(id):
    runlocation = Runlocation.query.get_or_404(id)
    if request.method == 'POST':
        if runlocation:
            runlocation.description = request.form.get('runlocation')
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('location_show_all'))
    return render_template('location_new.html')


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
