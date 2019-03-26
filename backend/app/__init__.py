# -*- encoding: utf-8 -*-

from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_restful import Resource, Api


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
app.config['DEBUG'] = True
app.config['TESTING'] = True
app.config['BOOTSTRAP_FONTAWESOME'] = True
app.config['SECRET_KEY'] = "MYSECRETKEY"
app.config['CSRF_ENABLED'] = False
db_uri = "postgres://application:application@localhost:5432/robotapp"
app.config['SQLALCHEMY_DATABASE_URI'] = db_uri

db = SQLAlchemy(app)  # flask-sqlalchemy
db.init_app(app)
api = Api(app)

from app.models import ApplicationUser, RoboticProcessAutomation, RobotRunEvent
from app.endpoints import *

