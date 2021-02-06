# This is Pythons import system.  It is what let's you
# use modules that other people(or yourself) wrote in your
# code!
from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager

# This tells Python to create an app for us.
# __name__ is a special value in python. For
# now, lets not worry too much about what it means.
app = Flask(__name__)
app.config.from_object("config.DevConfig")
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db = SQLAlchemy(app)
login_manager = LoginManager(app)

from models import User


@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)


# This is what is called a decorator in Python.  It
# allows us to wrap one function around another.  In
# this case it tells Flask to send anything sent to '/'
# to this function.


@app.route("/")
def hello_world():
    return render_template("index.html")


# We can add a variable to the route as well.  This is
# one way to pass information to our function.


@app.route("/<name>")
def hello_name(name):
    # This is how you can format a string in Python.
    # This says to replace {name} with the name from the URL
    return render_template("name.html", name=name)
