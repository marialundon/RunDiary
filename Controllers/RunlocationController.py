# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db
from flask_login import login_required
from flask_login import current_user


options_location = Blueprint('options_location', __name__)
new_location = Blueprint('new_location',__name__)
data_location = Blueprint('data_location',__name__)
delete_location = Blueprint('delete_location',__name__)
update_location = Blueprint('update_location',__name__)

@options_location.route('/location')
@login_required
def location_options():
    return render_template('location_options.html', Runlocation = Runlocation.query.all())

@data_location.route('/location/locationdata')
@login_required
def location_data():
    runlocation = Runlocation.query.filter_by(userid = current_user.id)
    return render_template('location_data.html',data = runlocation)

@new_location.route('/location/locationnew', methods = ['GET', 'POST'])
@login_required
def location_new():
    if request.method == 'POST':
        if not request.form.get('runlocation',''):
            flash('Please enter all the fields', 'error')
        else:
            runlocation = Runlocation(request.form.get('runlocation',''),userid = current_user.id)
            db.session.add(runlocation)
            db.session.commit()
            return redirect(url_for('data_location.location_data'))
    return render_template('location_new.html')

@delete_location.route('/location/locationdelete/<id>', methods=['POST','DELETE','GET'])
@login_required
def location_delete(id):
    runlocation = Runlocation.query.get_or_404(id)
    db.session.delete(runlocation)
    db.session.commit()
    return redirect(url_for('data_location.location_data'))

@update_location.route('/location/locationupdate/<id>', methods=["GET","POST"])
@login_required
def location_update(id):
    runlocation = Runlocation.query.get_or_404(id)
    if request.method == 'POST':
        if runlocation:
            runlocation.description = request.form.get('runlocation')
            db.session.commit()
            return redirect(url_for('data_location.location_data'))
    return render_template('location_new.html')