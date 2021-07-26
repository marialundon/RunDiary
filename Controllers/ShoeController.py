# pylint: disable=no-member
from Model.Run import Run
from Model.Runtype import Runtype
from Model.Runlocation import Runlocation
from Model.Shoe import Shoe
from flask import Blueprint, request, render_template, flash, url_for, redirect
from Model import db

options_shoe = Blueprint('options_shoe', __name__)
new_shoe = Blueprint('new_shoe',__name__)
data_shoe = Blueprint('data_shoe',__name__)
delete_shoe = Blueprint('delete_shoe',__name__)
update_shoe = Blueprint('update_shoe',__name__)

@options_shoe.route('/shoe')
def shoe_options():
    return render_template('shoe_options.html', Shoe = Shoe.query.all())

@data_shoe.route('/shoe/shoedata')
def shoe_data():
    shoe = Shoe.query.all()
    return render_template('shoe_data.html',data = shoe)

@new_shoe.route('/shoe/shoenew', methods = ['GET', 'POST'])
def shoe_new():
    if request.method == 'POST':
        if not request.form.get('shoe',''):
            flash('Please enter all the fields', 'error')
        else:
            shoe = Shoe(request.form.get('shoe',''))
            
            db.session.add(shoe)
            db.session.commit()
            return redirect(url_for('data_shoe.shoe_data'))
    return render_template('shoe_new.html')

@delete_shoe.route('/shoe/shoedelete/<id>', methods=['POST','DELETE','GET'])
def shoe_delete(id):
    shoe = Shoe.query.get_or_404(id)
    db.session.delete(shoe)
    db.session.commit()
    return redirect(url_for('data_shoe.shoe_data'))

@update_shoe.route('/shoe/shoeupdate/<id>', methods=["GET","POST"])
def shoe_update(id):
    shoe = Shoe.query.get_or_404(id)
    if request.method == 'POST':
        if shoe:

            shoe.description = request.form.get('shoe')

            db.session.commit()
            return redirect(url_for('data_shoe.shoe_data'))
    return render_template('shoe_new.html')

