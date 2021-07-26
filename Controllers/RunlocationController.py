# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db

options_location = Blueprint('options_location', __name__)
new_location = Blueprint('new_location',__name__)
data_location = Blueprint('data_location',__name__)
delete_location = Blueprint('delete_location',__name__)
update_location = Blueprint('update_location',__name__)

@options_location.route('/location')
def location_options():
    return render_template('location_options.html', Runlocation = Runlocation.query.all())

@data_location.route('/location/locationdata')
def location_data():
    runlocation = Runlocation.query.all()
    return render_template('location_data.html',data = runlocation)

@new_location.route('/location/locationnew', methods = ['GET', 'POST'])
def location_new():
    if request.method == 'POST':
        if not request.form.get('runlocation',''):
            flash('Please enter all the fields', 'error')
        else:
            runlocation = Runlocation(request.form.get('runlocation',''))
            db.session.add(runlocation)
            db.session.commit()
            return redirect(url_for('data_location.location_data'))
    return render_template('location_new.html')

@delete_location.route('/location/locationdelete/<id>', methods=['POST','DELETE','GET'])
def location_delete(id):
    runlocation = Runlocation.query.get_or_404(id)
    db.session.delete(runlocation)
    db.session.commit()
    return redirect(url_for('data_location.location_data'))

@update_location.route('/location/locationupdate/<id>', methods=["GET","POST"])
def location_update(id):
    runlocation = Runlocation.query.get_or_404(id)
    if request.method == 'POST':
        if runlocation:
            runlocation.description = request.form.get('runlocation')
            db.session.commit()
            return redirect(url_for('data_location.location_data'))
    return render_template('location_new.html')