# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from Model.Shoe import Shoe
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db
from sqlalchemy import desc
from flask_login import login_required
from flask_login import current_user

options_run = Blueprint('options_run', __name__)
new_run = Blueprint('new_run',__name__)
data_run = Blueprint('data_run',__name__)
recent_run = Blueprint('recent_run',__name__)
delete_run = Blueprint('delete_run',__name__)
update_run = Blueprint('update_run',__name__)

@options_run.route("/")
@login_required
def run_options():
    runs = Run.query.filter_by(userid = current_user.id).order_by(desc(Run.date)).limit(1)
    return render_template('run_options.html',recent = runs)

@new_run.route("/runs/new", methods=["GET","POST"])
@login_required
def run_new():
    if request.method == 'POST':
        if not request.form.get('typeofrun','') or not request.form.get('date','') or not request.form.get('shoe','') or not request.form.get('length','') or not request.form.get('time','') or not request.form.get('location',''):
            flash('Please enter all the fields', 'error')
        else:
            run = Run(request.form.get('typeofrun'),request.form.get('date'),request.form.get('length'),request.form.get('time'), request.form.get('location'),request.form.get('shoe'),userid = current_user.id)
            
            db.session.add(run)
            db.session.commit()
            return redirect(url_for('data_run.run_data'))
    return render_template('run_new.html', Runtype = Runtype.query.filter_by(userid = current_user.id),Runlocation = Runlocation.query.filter_by(userid = current_user.id),Shoe = Shoe.query.filter_by(userid = current_user.id))
    
@data_run.route('/runs/data')
@login_required
def run_data():
    runs = Run.query.filter_by(userid = current_user.id)
    return render_template('run_data.html',data = runs)

@delete_run.route('/runs/delete/<id>', methods=['POST','DELETE','GET'])
@login_required
def run_delete(id):
    run = Run.query.get_or_404(id)
    db.session.delete(run)
    db.session.commit()
    return redirect(url_for('data_run.run_data'))

@update_run.route('/runs/update/<id>', methods=["GET","POST"])
@login_required
def run_update(id):
    run = Run.query.get_or_404(id)
    if request.method == 'POST':
        if run:

            run.typeofrun = request.form.get('typeofrun')
            run.date= request.form.get('date')
            run.length = request.form.get('length')
            run.time = request.form.get('time')
            run.location = request.form.get('location')
            run.shoe = request.form.get('shoe')

            db.session.commit()
            return redirect(url_for('data_run.run_data'))
    return render_template('run_update.html',Runtype = Runtype.query.filter_by(userid = current_user.id), Runlocation = Runlocation.query.filter_by(userid = current_user.id),runtobeupdated=run,Shoe = Shoe.query.filter_by(userid = current_user.id))

