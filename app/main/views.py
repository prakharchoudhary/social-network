from datetime import datetime
from flask import render_template, session, redirect, url_for
from flask_login import login_required
from . import main


@main.route('/')
def index():
  return render_template('index.html')


@main.route('/secret')
@login_required
def secret():
  return 'Only authenticated users are allowed!'
