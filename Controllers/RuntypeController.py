# pylint: disable=no-member
from Model.Run import Runs
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db

show_type = Blueprint('show_type', __name__)
new_type = Blueprint('new_type',__name__)
data_type = Blueprint('data_type',__name__)
delete_type = Blueprint('delete_type',__name__)
update_type = Blueprint('update_type',__name__)

@show_type.route('/type')
def type_show_all():
    return render_template('type_show_all.html', Runtype = Runtype.query.all())

@data_type.route('/type/typedata')
def type_data():
    runtype = Runtype.query.all()
    return render_template('type_data.html',data = runtype)

@new_type.route('/type/typenew', methods = ['GET', 'POST'])
def type_new():
    if request.method == 'POST':
        if not request.form.get('runtype',''):
            flash('Please enter all the fields', 'error')
        else:
            runtype = Runtype(request.form.get('runtype',''))
            
            db.session.add(runtype)
            db.session.commit()
            flash('Run type was successfully added')
            return redirect(url_for('show_type.type_show_all'))
    return render_template('type_new.html')

@delete_type.route('/type/typedelete/<id>', methods=['POST','DELETE','GET'])
def type_delete(id):
    runtype = Runtype.query.get_or_404(id)
    db.session.delete(runtype)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('show_type.type_show_all'))

@update_type.route('/type/typeupdate/<id>', methods=["GET","POST"])
def type_update(id):
    runtype = Runtype.query.get_or_404(id)
    if request.method == 'POST':
        if runtype:

            runtype.description = request.form.get('runtype')

            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('show_type.type_show_all'))
    return render_template('type_new.html')

