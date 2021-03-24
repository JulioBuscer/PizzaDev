
# import datetime module
import datetime
# import pymongo module
import pymongo
import dns
# connection string
from flask import Blueprint, render_template, request, session, Flask
from flask.helpers import url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from flask_sqlalchemy import model
from werkzeug.utils import redirect
from . import db
from . import models
from flask_principal import Principal, Permission, RoleNeed

main = Blueprint('main', __name__)


@main.route('/')
def index():

    if RoleNeed('admin'):
        admin = True
        return render_template('index.html', admin=admin)
    if RoleNeed('admin'):
        cliente = True
        return render_template('index.html', cliente=cliente)
    return render_template('index.html')


@main.route('/recetario')
def recetario():
    return render_template("recetario.html")


@main.route('/registroRecetario')
def registroRecetario():
    return render_template("registrarRecetario.html")