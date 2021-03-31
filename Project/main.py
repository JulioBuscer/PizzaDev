
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
from . import dbSQL, dbMongo
from . import models
from .models import Proveedor
from flask_principal import Principal, Permission, RoleNeed

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.has_role('admin'):
        admin = True
        return render_template('index.html', admin=admin)
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('index.html', cliente=cliente)
    return render_template('index.html')


@main.route("/usuario")
def mostrarDatosUsuario():
    return render_template("usuario.html")

@main.route("/proveedores")
def proveedores():
    return render_template("proveedores.html")

@main.route('/registrarProveedor',methods=['GET'])
def registrarProveedor():
    return render_template('registrarProveedor.html')

@main.route('/guardarProveedor',methods=['GET','POST'])
def guardarProveedor():
    
    if request.method=='POST':
        # print(request.form.get("txtEmpresa"))
        pro=models.Proveedor(
            empresa=request.form.get("txtEmpresa"),
            direccionPro=request.form.get("txtDireccion"),
            email=request.form.get("txtEmail"),
            representante=request.form.get("txtRepresentante"),
            telefono=request.form.get("txtTelefono"))
        dbSQL.session.add(pro)
        dbSQL.session.commit()
    return render_template('proveedores.html')

@main.route('/registrarUsuario',methods=['GET','POST'])
def registrarUsuario():
    return render_template('registrarUsuario.html')

@main.route('/ventas')
def ventas():
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('ventas.html', cliente=cliente)
    return render_template('index.html')


@main.route('/admin/ventas')
def admin_ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('admin/ventas.html', admin=admin)
    return render_template('index.html')


@main.route('/recetario')
def recetario():
    return render_template("recetario.html")


@main.route('/registroRecetario')
def registroRecetario():
    return render_template("registrarRecetario.html")
