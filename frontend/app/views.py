# -*- encoding: utf-8 -*-
"""
Python Aplication Template
Licence: GPLv3
"""

from flask import url_for, redirect, render_template, flash, g, session, jsonify
from flask.ext.login import login_user, logout_user, current_user, login_required
from app import app, lm
from forms import ExampleForm, LoginForm


@app.route('/')
# @login_required
def index():
	flash("Welcome!", "alert alert-primary")
	return render_template('index.html')

@app.route('/create')
# @login_required
def create():
	return render_template('create.html')

@app.route('/list')
# @login_required
def table_list():
	return render_template('list.html')


@app.route('/events')
# @login_required
def events():
	return render_template('events.html')

@app.route('/microservice')
# @login_required
def microservice():
	return render_template('microservice.html')

@app.route('/api/data')
# @login_required
def api_data():
	data = {"messages":["hello world", "goodbye world"]}
	return jsonify(data)
# ====================
