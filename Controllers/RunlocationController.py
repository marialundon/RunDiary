# pylint: disable=no-member
from Model.Run import Runs
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db

show_location = Blueprint('show_location', __name__)
new_location = Blueprint('new_location',__name__)
data_location = Blueprint('data_location',__name__)
delete_location = Blueprint('delete_location',__name__)
update_location = Blueprint('update_location',__name__)

@show_location.route('/location')
def location_show_all():
    return render_template('location_show_all.html', Runlocation = Runlocation.query.all())

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
            flash('Run type was successfully added')
            return redirect(url_for('show_location.location_show_all'))
    return render_template('location_new.html')

@delete_location.route('/location/locationdelete/<id>', methods=['POST','DELETE','GET'])
def location_delete(id):
    runlocation = Runlocation.query.get_or_404(id)
    db.session.delete(runlocation)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('show_location.location_show_all'))

@update_location.route('/location/locationupdate/<id>', methods=["GET","POST"])
def location_update(id):
    runlocation = Runlocation.query.get_or_404(id)
    if request.method == 'POST':
        if runlocation:
            runlocation.description = request.form.get('runlocation')
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('show_location.location_show_all'))
    return render_template('location_new.html')