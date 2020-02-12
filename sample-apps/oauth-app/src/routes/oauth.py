from flask import Blueprint, render_template, redirect

module = Blueprint(__name__, __name__)


@module.route('/')
@module.route('/oauth/login')
def login():
    return render_template('oauth/login.html')


@module.route('/oauth/authorize')
def authorize():
    pass
