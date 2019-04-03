import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

from tools.dummy_db import create_dummies

app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_HOST'],27017)
db = client.profiles

@app.route('/')
def home():
    return render_template('home.html', page='home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ route that handles registration form submission
        by inserting new document in database
        #TODO: add security!
    """
    if request.method == 'POST':
        profile_doc = {
            'first_name': request.form['first_name'],
            'surname': request.form['surname'],
            'email': request.form['email'],
            'orcid': request.form['orcid'],
            'github': request.form['github'],
            'institution_url': request.form['institution_url'],
            'disciplines': request.form.getlist('disciplines'),
            'languages': request.form.getlist('languages')
        }
        db.profiles.insert_one(profile_doc)
        return redirect(url_for('confirm'))
    else:
        return render_template('register.html', page='register')

@app.route("/dummy", methods=["GET", "POST"])
def register_dummies():
    """ Insert dummy records in the database
    """
    if request.method == "POST":
        number = request.form["number"]
        prof = create_dummies(int(number))
        db.profiles.insert_many(prof)
        return redirect(url_for("test"))
    else:
        return render_template("dummy.html")
@app.route('/confirm')
def confirm():
    """ route that outputs confirmation of registration
        #TODO: mechanism to determine if registration successful!
    """
    return render_template('confirm.html', page='confirmation')

@app.route('/search')
def search():
    """ #TODO: search view renders search form
    """
    return render_template('search.html')

@app.route('/results', methods=['GET', 'POST'])
def results():
    _profiles = db.profiles.find()
    profiles = [profile for profile in _profiles]
    return render_template('results.html', profiles=profiles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
