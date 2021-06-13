# pylint: disable=no-member 
from flask import Flask, render_template, request, flash, url_for, redirect
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import ForeignKey

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"

db = SQLAlchemy(app)

class Runs(db.Model):
    __tablename__ = 'runs'
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

@app.route('/runs/new', methods = ['GET', 'POST'])
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


@app.route('/runs/data')
def rundata():
    runs = Runs.query.all()
    return render_template('data.html',data = runs)

@app.route('/runs/delete', methods=['POST','DELETE','GET'])
def delete_run_via_code():
    run = Runs.query.filter_by(typeofrun = 'Easy run').all()
    for item in run:
        db.session.delete(item)
        db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('show_all'))

@app.route('/runs/delete/<id>', methods=['POST','DELETE','GET'])
def delete(id):
    run = Runs.query.get_or_404(id)
    db.session.delete(run)
    db.session.commit()
    flash('Item deleted.')
    return redirect(url_for('show_all'))

@app.route('/runs/update', methods=["GET","POST"])
def update_via_code():
    run = Runs.query.filter_by(id = '2').first()
    run.id = '2'
    db.session.commit()
    flash('Item updated')
    return redirect(url_for('show_all'))

@app.route('/runs/update/<id>', methods=["GET","POST"])
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

class Runtype(db.Model):
    __tablename__ = 'runtype'
    id = db.Column('runtype_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))

    def __init__(self, description):
        self.description = description

@app.route('/runtype')
def show_all_runtype():
    return render_template('runtypeshow_all.html', Runtype = Runtype.query.all())

@app.route('/runtype/runtypedata')
def runtypedata():
    runtype = Runtype.query.all()
    return render_template('runtypedata.html',data = runtype)

@app.route('/runtype/runtypenew', methods = ['GET', 'POST'])
def runtypenew():
    if request.method == 'POST':
        if not request.form.get('runtype',''):
            flash('Please enter all the fields', 'error')
        else:
            runtype = Runtype(request.form.get('runtype',''))
            
            db.session.add(runtype)
            db.session.commit()
            flash('Run type was successfully added')
            return redirect(url_for('show_all_runtype'))
    return render_template('runtypenew.html')

@app.route('/runtype/runtypedelete/<id>', methods=['POST','DELETE','GET'])
def runtypedelete(id):
    runtype = Runtype.query.get_or_404(id)
    db.session.delete(runtype)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('show_all_runtype'))

@app.route('/runtype/runtypeupdate/<id>', methods=["GET","POST"])
def runtypeupdate(id):
    runtype = Runtype.query.get_or_404(id)
    if request.method == 'POST':
        if runtype:
            db.session.delete(runtype)
            db.session.commit()

            runtype = Runtype(request.form.get('runtype'))

            db.session.add(runtype)
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('show_all_runtype'))
    return render_template('runtypenew.html')

class Runlocation(db.Model):
    __tablename__ = 'runlocation'
    id = db.Column('runlocation_id', db.Integer, primary_key = True)
    description = db.Column(db.String(100))

    def __init__(self, description):
        self.description = description

@app.route('/runlocation')
def show_all_location():
    return render_template('runlocationshow_all.html', Runlocation = Runlocation.query.all())

@app.route('/runlocation/runlocationdata')
def runlocationdata():
    runlocation = Runlocation.query.all()
    return render_template('runlocationdata.html',data = runlocation)

@app.route('/runlocation/runlocationnew', methods = ['GET', 'POST'])
def runlocationnew():
    if request.method == 'POST':
        if not request.form.get('runlocation',''):
            flash('Please enter all the fields', 'error')
        else:
            runlocation = Runlocation(request.form.get('runlocation',''))
            
            db.session.add(runlocation)
            db.session.commit()
            flash('Run type was successfully added')
            return redirect(url_for('show_all_location'))
    return render_template('runlocationnew.html')

@app.route('/runlocation/runlocationdelete/<id>', methods=['POST','DELETE','GET'])
def runlocationdelete(id):
    runlocation = Runlocation.query.get_or_404(id)
    db.session.delete(runlocation)
    db.session.commit()
    flash('Run type deleted.')
    return redirect(url_for('show_all_location'))

@app.route('/runlocation/runlocationupdate/<id>', methods=["GET","POST"])
def runlocationupdate(id):
    runlocation = Runlocation.query.get_or_404(id)
    if request.method == 'POST':
        if runlocation:
            db.session.delete(runlocation)
            db.session.commit()

            runlocation = Runlocation(request.form.get('runlocation'))

            db.session.add(runlocation)
            db.session.commit()
            flash('Record was successfully updated')
            return redirect(url_for('show_all_location'))
    return render_template('runlocationnew.html')


if __name__ == '__main__':
    db.create_all()
    app.run(debug = True)
