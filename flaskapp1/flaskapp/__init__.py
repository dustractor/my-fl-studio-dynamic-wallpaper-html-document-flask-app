import flask

print("Flask imported")

app = flask.Flask(__package__)

print("app created")

from . import views
