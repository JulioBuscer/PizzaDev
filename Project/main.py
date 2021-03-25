
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


@main.route("/usuario")
def mostrarDatosUsuario():
    return render_template("usuario.html")

@main.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")

@main.route('/registrarProveedor',methods=['GET','POST'])
def registrarProveedor():
    return render_template('registrarProveedor.html')