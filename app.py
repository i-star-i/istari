import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient(os.environ['MONGODB_HOST'],27017)
db = client.profiles

@app.route('/')
def home():
    return render_template('home.html', page='home')

@app.route('/register', methods=['GET', 'POST'])
def register():
    """ #TODO: route that handles register form submission
        by inserting new document in database
    """
    if request.method == 'POST':
        profile_doc = {
            'name': request.form['name'],
            'github_username': request.form['github_username']
        }
        db.profiles.insert_one(profile_doc)
        return redirect(url_for('confirm'))
    else:
        return render_template('register.html')

@app.route('/confirm')
def confirm():
    return "#TODO confirmation of registration page"

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
