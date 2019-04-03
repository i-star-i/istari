import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

app = Flask(__name__)

client = MongoClient('eab092bcc2ca', 27017)
db = client.tododb

@app.route('/')
def hello():
    return "hello world from a Docker container"

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
        return redirect(url_for('test'))
    else:
        return render_template('register.html')


@app.route('/test')
def test():
    """ #TODO: delete this
        dummy view to check stuff is connected
    """
    _profiles = db.profiles.find()
    profiles = [profile for profile in _profiles]
    return render_template('test.html', profiles=profiles)

if __name__ == "__main__":
    app.run(host='0.0.0.0', debug=True)
