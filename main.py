# pylint: disable=no-member 

from Controllers.RunController import show_run
from Model.Run import Runs
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

@app.route('/runs/new', methods = ['GET', 'POST'])
def run_new():
    if request.method == 'POST':
        if not request.form.get('typeofrun','') or not request.form.get('length','') or not request.form.get('location','') or not request.form.get('time',''):
            flash('Please enter all the fields', 'error')
        else:
            run = Runs(request.form.get('typeofrun',''), request.form.get('length',''),request.form.get('location',''), request.form.get('time',''))
            
            db.session.add(run)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('run_show_all'))
    return render_template('run_new.html',Runtype = Runtype.query.all(), Runlocation = Runlocation.query.all())


@app.route('/runs/data')
def run_data():
    runs = Runs.query.all()
    return render_template('run_data.html',data = runs)

@app.route('/runs/delete/<id>', methods=['POST','DELETE','GET'])
def run_delete(id):
    run = Runs.query.get_or_404(id)
    db.session.delete(run)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('run_show_all'))

@app.route('/runs/update/<id>', methods=["GET","POST"])
def run_update(id):
    run = Runs.query.get_or_404(id)
    if request.method == 'POST':
        if run:

            run.typeofrun = request.form.get('typeofrun')
            run.length = request.form.get('length')
            run.location = request.form.get('location')
            run.time = request.form.get('time')

            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('run_show_all'))
    return render_template('run_update.html',Runtype = Runtype.query.all(), Runlocation = Runlocation.query.all(),runtobeupdated=run)

class Runtype(db.Model):
    __tablename__ = 'runtype'
    id = db.Column('runtype_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))
    

    def __init__(self, description):
        self.description = description

@app.route('/type')
def type_show_all():
    return render_template('type_show_all.html', Runtype = Runtype.query.all())

@app.route('/type/typedata')
def type_data():
    runtype = Runtype.query.all()
    return render_template('type_data.html',data = runtype)

@app.route('/type/typenew', methods = ['GET', 'POST'])
def type_new():
    if request.method == 'POST':
        if not request.form.get('runtype',''):
            flash('Please enter all the fields', 'error')
        else:
            runtype = Runtype(request.form.get('runtype',''))
            
            db.session.add(runtype)
            db.session.commit()
            flash('Run type was successfully added')
            return redirect(url_for('type_show_all'))
    return render_template('type_new.html')

@app.route('/type/typedelete/<id>', methods=['POST','DELETE','GET'])
def type_delete(id):
    runtype = Runtype.query.get_or_404(id)
    db.session.delete(runtype)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('type_show_all'))

@app.route('/type/typeupdate/<id>', methods=["GET","POST"])
def type_update(id):
    runtype = Runtype.query.get_or_404(id)
    if request.method == 'POST':
        if runtype:

            runtype.description = request.form.get('runtype')

            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('type_show_all'))
    return render_template('type_new.html')

class Runlocation(db.Model):
    __tablename__ = 'runlocation'
    id = db.Column('runlocation_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))

    def __init__(self, description):
        self.description = description

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
