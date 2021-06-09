# pylint: disable=no-member 
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)
class Runs(db.Model):
    id = db.Column('run_id', db.Integer, primary_key = True)
    typeofrun = db.Column(db.String(100))
    length = db.Column(db.String(50))
    location = db.Column(db.String(200))
    time = db.Column(db.String(10))

    def __init__(self, typeofrun, length, location, time):
        self.typeofrun = typeofrun
        self.length = length
        self.location = location
        self.time = time


@app.route('/')
def show_all():
    return render_template('show_all.html', Runs = Runs.query.all())

@app.route('/new', methods = ['GET', 'POST'])
def new():
    if request.method == 'POST':
        if not request.form.get('typeofrun','') or not request.form.get('length','') or not request.form.get('location','') or not request.form.get('time',''):
            flash('Please enter all the fields', 'error')
        else:
            run = Runs(request.form.get('typeofrun',''), request.form.get('length',''),request.form.get('location',''), request.form.get('time',''))
            
            db.session.add(run)
            db.session.commit()
            flash('Record was successfully added')
            return redirect(url_for('show_all'))
    return render_template('new.html')


@app.route('/data')
def data():
    runs = Runs.query.all()
    return render_template('data.html',data = runs)

@app.route('/data/delete', methods=['POST','DELETE','GET'])
def delete_run_via_code():
    run = Runs.query.filter_by(typeofrun = 'Easy run').all()
    for item in run:
        db.session.delete(item)
        db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('show_all'))

@app.route('/data/delete/<id>', methods=['POST','DELETE','GET'])
def delete(id):
    run = Runs.query.get_or_404(id)
    db.session.delete(run)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('show_all'))

@app.route('/data/update', methods=["GET","POST"])
def update_via_code():
    run = Runs.query.filter_by(id = '2').first()
    run.id = '2'
    db.session.commit()
    flash('Item updated')
    return redirect(url_for('show_all'))

@app.route('/data/update/<id>', methods=["GET","POST"])
def update(id):
    run = Runs.query.get_or_404(id)
    if request.method == 'POST':
        if run:
            db.session.delete(run)
            db.session.commit()

            run = Runs(request.form.get('typeofrun'), request.form.get('length'),request.form.get('location'), request.form.get('time'))

            db.session.add(run)
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('show_all'))
    return render_template('new.html')

if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
