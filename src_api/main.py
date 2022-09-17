import json
from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api





# Create a new App
app = Flask(__name__)

# Flask & SQLAlchemy configs 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

# SQLAlchemy DB config for using mysql database
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql+pymysql://foxy:cisco12345@zfs_mysql_db/fox_sheets'

app.secret_key = "glitch"

# create new Api
api = Api(app)


# Initialize the database
db = SQLAlchemy(app)

# Create the database model (table) to store the cheat sheets
class SheetsDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String(32))
    what = db.Column(db.String(256))
    how = db.Column(db.String(256))

##########################################################################
    # ADD A METHOD HERE TO RETURN A PYTHON DICT OF THE OBJECT PROPERTIES
    # def return_pyDict(self):
##########################################################################

# ENDPOINT TO ACCEPT A LIST OF OBJECTS REPRESENTING SHEETS
class Batch_Imports(Resource):
    def post(self):
        sheets = request.get_json()
        for sheet in sheets:
            entry = SheetsDB(group=sheet["group"], how=sheet["how"], what=sheet["what"])
            db.session.add(entry)
            db.session.commit()
        
        return 201

# ENDPOINT TO RETREIVE ALL THE SHEETS IN THE DB
class Retrv_All_Sheets(Resource):
    def get(self):
        sheets = SheetsDB.query.all()
        for item in sheets:
            break
        return item



api.add_resource(Batch_Imports, '/batch_imports') # http://[host]:6729/batch_imports
api.add_resource(Retrv_All_Sheets, '/rtrv_all_sheets') # http://[host]:6729/rtrv_all_sheets



#######################################################   
app.run(host ='0.0.0.0', port = 6729, debug = True) 