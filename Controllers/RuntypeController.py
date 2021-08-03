# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db
from flask_login import login_required
from flask_login import current_user

options_type = Blueprint('options_type', __name__)
new_type = Blueprint('new_type',__name__)
data_type = Blueprint('data_type',__name__)
delete_type = Blueprint('delete_type',__name__)
update_type = Blueprint('update_type',__name__)

@options_type.route('/type')
@login_required
def type_options():
    return render_template('type_options.html', Runtype = Runtype.query.all())

@data_type.route('/type/typedata')
@login_required
def type_data():
    runtype = Runtype.query.filter_by(userid = current_user.id)
    return render_template('type_data.html',data = runtype)

@new_type.route('/type/typenew', methods = ['GET', 'POST'])
@login_required
def type_new():
    if request.method == 'POST':
        if not request.form.get('runtype',''):
            flash('Please enter all the fields', 'error')
        else:
            runtype = Runtype(request.form.get('runtype',''),userid = current_user.id)
            
            db.session.add(runtype)
            db.session.commit()
            return redirect(url_for('data_type.type_data'))
    return render_template('type_new.html')

@delete_type.route('/type/typedelete/<id>', methods=['POST','DELETE','GET'])
@login_required
def type_delete(id):
    runtype = Runtype.query.get_or_404(id)
    db.session.delete(runtype)
    db.session.commit()
    return redirect(url_for('data_type.type_data'))

@update_type.route('/type/typeupdate/<id>', methods=["GET","POST"])
@login_required
def type_update(id):
    runtype = Runtype.query.get_or_404(id)
    if request.method == 'POST':
        if runtype:

            runtype.description = request.form.get('runtype')

            db.session.commit()
            return redirect(url_for('data_type.type_data'))
    return render_template('type_new.html')

