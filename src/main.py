from flask import Flask, redirect, url_for, render_template, request, flash
from flask_sqlalchemy import SQLAlchemy





# Create a new App
app = Flask(__name__)

# Flask & SQLAlchemy configs 
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///cheat_sheets.db'
app.secret_key = "glitch"

# Initialize the database
db = SQLAlchemy(app)

# Create the database model (table) to store the cheat sheets
class SheetsDB(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    group = db.Column(db.String)
    what = db.Column(db.String)
    how = db.Column(db.String)




# ENDPOINT TO ADD A CHEAT SHEET ENTRY TO THE DATABASE
@app.route('/', methods=["POST", "GET"])
def home():

# If the method in the request is "POST", extract values from the returned form
    if request.method == "POST":
        group = request.form["group"]
        what = request.form["what"]
        how = request.form["how"]
# Validate if that cheat sheet is not already in the database
        # sheet = SheetsDB.query.filter_by(how=how)
        # if sheet == None:

# Create a database object from the values
        sheet = SheetsDB(group=group, how=how, what=what)

# Use the method from the database object to enter the values into the database
        db.session.add(sheet)
        db.session.commit()

# Return a message to the user that the cheat sheet was entered into the database
        flash('The Cheat Sheet was Added', category='info')
        return render_template("index.html")
# Return a flash message if the cheat sheet is already in the database
        # else:
        #     flash('This Cheat Sheet Already Exist', category='info')
        #     return render_template("index.html")

# If the method in the request is "GET" render the "index.html" page 
    else:    
        return render_template("index.html")




# ENDPOINT TO SEARCH FOR CHEAT SHEET ENTRIES FROM THE DATABASE & RETURN RESULTS TO USER
@app.route('/search', methods=["POST"])
def search():

# Extract search keywork from the returned form
    search_kword = request.form["search_kword"]

# Use search keyword to query/filter thru the database to matching cheat sheet entries
    # sheets = SheetsDB.query.filter_by(what=search_kword)
    like_string_arg = f'%{search_kword}%'
    sheets = SheetsDB.query.filter(SheetsDB.how.like(like_string_arg))

    # how = sheets.["how"]
    # type_value = type(sheets)


# Return all matching cheat sheet entries back to the user
    # return f'{search_kword}'  
    return render_template("test_results.html", sheets=sheets) 



# SELECT "sheetsDB".id AS "sheetsDB_id", "sheetsDB"."group" AS "sheetsDB_group", "sheetsDB".what AS "sheetsDB_what", "sheetsDB".how AS "sheetsDB_how" FROM "sheetsDB" WHERE "sheetsDB".what = ?






#######################################################   
if __name__ == '__main__':
    # from db import db
    app.run(host ='0.0.0.0', port = 2584, debug = True) 