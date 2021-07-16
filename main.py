# pylint: disable=no-member 

from Controllers.RunController import options_run,new_run, data_run, update_run, delete_run
from Controllers.RuntypeController import options_type,new_type, data_type, update_type, delete_type
from Controllers.ShoeController import options_shoe,new_shoe, data_shoe, update_shoe, delete_shoe
from Controllers.RunlocationController import options_location,new_location, data_location, update_location, delete_location
from flask import Flask
from Model import db

app = Flask (__name__)
app.config ['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///runs.sqlite3'
app.config['SECRET_KEY'] = "123456789"
db.init_app(app)

app.register_blueprint(options_run)

app.register_blueprint(new_run)

app.register_blueprint(data_run)

app.register_blueprint(update_run)

app.register_blueprint(delete_run)

app.register_blueprint(options_type)

app.register_blueprint(new_type)

app.register_blueprint(data_type)

app.register_blueprint(update_type)

app.register_blueprint(delete_type)

app.register_blueprint(options_shoe)

app.register_blueprint(new_shoe)

app.register_blueprint(data_shoe)

app.register_blueprint(update_shoe)

app.register_blueprint(delete_shoe)

app.register_blueprint(options_location)

app.register_blueprint(new_location)

app.register_blueprint(data_location)

app.register_blueprint(update_location)

app.register_blueprint(delete_location)



if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug = True)
