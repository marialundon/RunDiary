# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db
from sqlalchemy import desc

options_run = Blueprint('options_run', __name__)
new_run = Blueprint('new_run',__name__)
data_run = Blueprint('data_run',__name__)
recent_run = Blueprint('recent_run',__name__)
delete_run = Blueprint('delete_run',__name__)
update_run = Blueprint('update_run',__name__)

@options_run.route("/")
def run_options():
    runs = Run.query.order_by(desc(Run.date)).limit(1)
    return render_template('run_options.html',recent = runs)

@new_run.route("/runs/new", methods=["GET","POST"])
def run_new():
    if request.method == 'POST':
        if not request.form.get('typeofrun','') or not request.form.get('date','') or not request.form.get('length','') or not request.form.get('time','') or not request.form.get('location',''):
            flash('Please enter all the fields', 'error')
        else:
            run = Run(request.form.get('typeofrun'),request.form.get('date'),request.form.get('length'),request.form.get('time'), request.form.get('location'))
            
            db.session.add(run)
            db.session.commit()
            print('Hello')
            flash('Record was successfully added')
            return redirect(url_for('options_run.run_options'))
    return render_template('run_new.html', Runtype = Runtype.query.all(),Runlocation = Runlocation.query.all())
    
@data_run.route('/runs/data')
def run_data():
    runs = Run.query.all()
    return render_template('run_data.html',data = runs)

@delete_run.route('/runs/delete/<id>', methods=['POST','DELETE','GET'])
def run_delete(id):
    run = Run.query.get_or_404(id)
    db.session.delete(run)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('options_run.run_options'))

@update_run.route('/runs/update/<id>', methods=["GET","POST"])
def run_update(id):
    run = Run.query.get_or_404(id)
    if request.method == 'POST':
        if run:

            run.typeofrun = request.form.get('typeofrun')
            run.date= request.form.get('date')
            run.length = request.form.get('length')
            run.time = request.form.get('time')
            run.location = request.form.get('location')

            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('options_run.run_options'))
    return render_template('run_update.html',Runtype = Runtype.query.all(), Runlocation = Runlocation.query.all(),runtobeupdated=run)

