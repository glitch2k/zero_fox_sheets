from flask import Flask, redirect, url_for, render_template, request, flash
import json
from addict import Dict









# Create a new App
app = Flask(__name__)




# ENDPOINT TO ADD A CHEAT SHEET ENTRY TO THE DATABASE
@app.route('/', methods=["POST", "GET"])
def home():

# Extract values from the returned form
    if request.method == "POST":
        group = request.form["group"]
        what = request.form["what"]
        how = request.form["how"]

# Create a database object from the values
    
     

# Use the method from the database object to enter the values into the database



# Return a message to the user that the cheat sheet was entered into the database
        return # return rendered_template with message to user that the cheat sheet entry was made 
    else:    
        return render_template("index.html")




# ENDPOINT TO SEARCH FOR CHEAT SHEET ENTRIES FROM THE DATABASE & RETURN RESULTS TO USER
@app.route('/search', methods=["POST"])
def search():

# Extract search keywork from the returned form
    search_kword = request.form["search_kword"]

# Use search keyword to query/filter thru the database to matching cheat sheet entries


# Return all matching cheat sheet entries back to the user
    return # return rendered_template with matching cheat sheet entries 










#######################################################   
if __name__ == '__main__':
    app.run(host ='0.0.0.0', port = 2584, debug = True) 