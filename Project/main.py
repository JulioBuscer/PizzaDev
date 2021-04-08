
# import datetime module
import datetime
# import pymongo module
# import pymongo
import dns
# connection string
from flask import Blueprint, render_template, request, session, Flask
from flask.helpers import url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from flask_sqlalchemy import model
from werkzeug.utils import redirect
from . import dbSQL
from . import models
from flask_principal import Principal, Permission, RoleNeed

main = Blueprint('main', __name__)


@main.route('/')
def index():
    if current_user.has_role('admin'):
        admin = True
        return render_template('index.html', admin=admin, name=current_user.name)
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('index.html', cliente=cliente, name=current_user.name)
    return render_template('index.html')


@main.route("/usuario")
def usuario():
    if current_user.has_role('admin'):
        admin = True
        usu = models.User.query.filter(models.User.active == 1).all()
        usu1 = models.User.query.filter(models.User.active == 0).all()
        return render_template("usuario.html", usuarios=usu, usuarios1=usu1, admin=admin)
    return redirect(url_for('main.index'))


@main.route("/proveedores")
def proveedores():
    if current_user.has_role('admin'):
        admin = True
        pro = models.Proveedor.query.filter(models.Proveedor.active == 1).all()
        pro1 = models.Proveedor.query.filter(
            models.Proveedor.active == 0).all()
        return render_template("proveedores.html", proveedores=pro, proveedores1=pro1, admin=admin)
    return redirect(url_for('main.index'))

@main.route('/registrarProveedor', methods=['GET'])
def registrarProveedor():
    if current_user.has_role('admin'):
        admin = True
        return render_template('registrarProveedor.html', admin=admin)
    return redirect(url_for('main.index'))

@main.route('/guardarProveedor', methods=['GET', 'POST'])
def guardarProveedor():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'POST':
            pro = models.Proveedor(
                empresa=request.form.get("txtEmpresa"),
                direccionPro=request.form.get("txtDirección"),
                email=request.form.get("txtEmail"),
                representante=request.form.get("txtRepresentante"),
                telefono=request.form.get("txtTelefono"))
            dbSQL.session.add(pro)
            dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))

@main.route("/modificarProveedor", methods=['POST', 'GET'])
def modificarProveedor():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("idProveedor1")
            pro = dbSQL.session.query(models.Proveedor).filter(
                models.Proveedor.idProveedor == id).first()
            print("AQUI")
            print(request.args.get("txtEmpresa1"))
            pro.empresa = request.args.get("txtEmpresa1")
            pro.direccionPro = request.args.get("txtDirección1")
            pro.email = request.args.get("txtEmail1")
            pro.representante = request.args.get("txtTelefono1")
            pro.telefono = request.args.get("txtRepresentante1")
            dbSQL.session.add(pro)
            dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))

@main.route('/activarrProveedor', methods=['GET', 'POST'])
def activarrProveedor():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("idProveedor")
            pro = dbSQL.session.query(models.Proveedor).filter(
                models.Proveedor.idProveedor == id).first()
        pro.active = 1
        dbSQL.session.add(pro)
        dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))

@main.route('/eliminarProveedor', methods=['GET', 'POST'])
def eliminarProveedor():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("idProveedor")
            pro = dbSQL.session.query(models.Proveedor).filter(
                models.Proveedor.idProveedor == id).first()
        pro.active = 0
        dbSQL.session.add(pro)
        dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))

# @main.route("/modificarProveedor", methods=['POST', 'GET'])
# def modificarProveedor():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("idProveedor1")
            pro = dbSQL.session.query(models.Proveedor).filter(
                models.Proveedor.idProveedor == id).first()
            print("AQUI")
            print(request.args.get("txtEmpresa1"))
            pro.empresa = request.args.get("txtEmpresa1")
            pro.direccionPro = request.args.get("txtDirección1")
            pro.email = request.args.get("txtEmail1")
            pro.representante = request.args.get("txtTelefono1")
            pro.telefono = request.args.get("txtRepresentante1")
            dbSQL.session.add(pro)
            dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))

@main.route('/activarrUsuario', methods=['GET', 'POST'])
def activarrUsuario():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("id")
            user = dbSQL.session.query(models.User).filter(
                models.User.id == id).first()
        user.active = 1
        dbSQL.session.add(user)
        dbSQL.session.commit()
        return redirect(url_for('main.usuario'))
    return redirect(url_for('main.index'))


@main.route('/eliminarUsuario', methods=['GET', 'POST'])
def eliminarUsuario():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("id")
            user = dbSQL.session.query(models.User).filter(
                models.User.id == id).first()
        user.active = 0
        dbSQL.session.add(user)
        dbSQL.session.commit()
        return redirect(url_for('main.usuario'))
    return redirect(url_for('main.index'))


@ main.route('/guardarUsuario', methods=['GET', 'POST'])
def guardarUsuario():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'POST':
            pro = models.Proveedor(
                empresa=request.form.get("txtEmpresa"),
                direccionPro=request.form.get("txtDirección"),
                email=request.form.get("txtEmail"),
                representante=request.form.get("txtRepresentante"),
                telefono=request.form.get("txtTelefono"))
            dbSQL.session.add(pro)
            dbSQL.session.commit()
        return redirect(url_for('main.proveedores'))
    return redirect(url_for('main.index'))


@main.route("/modificarUsuario", methods=['POST', 'GET'])
def modificarUsuario():
    if request.method == 'GET':
        id = request.args.get("id")
        user = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        return render_template("modificar.html", alumno=alum)
    if request.method == 'POST':
        id = request.form.get("id")
        alum = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        alum.nombre = request.form.get("txtNombre")
        alum.apaterno = request.form.get("txtApaterno")
        alum.amaterno = request.form.get("txtAmaterno")
        alum.email = request.form.get("txtMail")
        alum.email = request.form.get("txtPassword")
        dbSQL.session.add(alum)
        dbSQL.session.commit()
    return redirect(url_for('mostrarDatos'))


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
