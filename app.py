import os
from flask import Flask, redirect, url_for, request, render_template
from pymongo import MongoClient

from tools.dummy_db import create_dummies

app = Flask(__name__)

# client = MongoClient('eab092bcc2ca', 27017)
client = MongoClient(os.environ["MONGODB_HOST"], 27017)
db = client.profiles


@app.route("/")
def hello():
    return "hello world from a Docker container"


@app.route("/register", methods=["GET", "POST"])
def register():
    """ #TODO: route that handles register form submission
        by inserting new document in database
    """
    if request.method == "POST":
        profile_doc = {
            "name": request.form["name"],
            "github_username": request.form["github_username"],
        }
        db.profiles.insert_one(profile_doc)
        return redirect(url_for("test"))
    else:
        return render_template("register.html")


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


@app.route("/test")
def test():
    """ #TODO: delete this
        dummy view to check stuff is connected
    """
    _profiles = db.profiles.find()
    profiles = [profile for profile in _profiles]
    return render_template("test.html", profiles=profiles)


if __name__ == "__main__":
    import sys
    sys.path.insert(0, os.path.abspath('.'))

    app.run(host="0.0.0.0", debug=True)
