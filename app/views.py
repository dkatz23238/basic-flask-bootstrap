# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from forms import ExampleForm, LoginForm
from models import User


@app.route('/')
# @login_required
def index():
	return render_template('index.html')

@app.route('/list')
# @login_required
def table_list():
	return render_template('list.html')

@app.route('/microservice')
# @login_required
def microservice():
	return render_template('microservice.html')
# ====================
