
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
    usu = models.User.query.all()
    return render_template("usuario.html",usuarios = usu)

@main.route("/proveedores")
def proveedores():
    pro = models.Proveedor.query.all()
    return render_template("proveedores.html",proveedores = pro)

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

@main.route("/modificarProveedor",methods=['POST','GET'])
def modificarProveedor():
    if request.method == 'GET':
        id = request.args.get("id")
        proveedor = dbSQL.session.query(models.Proveedor).filter(models.Proveedor.idProveedor == id).first()
        print(proveedor.empresa)
        return render_template("registrarProveedor.html", proveedor=proveedor)
    if request.method == 'POST':
        id = request.form.get("id")
        pro = db.session.query(models.Proveedor).filter(models.Proveedor.idProveedor==id).first()
        pro.empresa = request.form.get("txtEmpresa")
        pro.direccionPro = request.form.get("txtDireccion")
        pro.email = request.form.get("txtEmail")
        pro.representante = request.form.get("txtTelefono")
        pro.telefono = request.form.get("txtRepresentante")
        dbSQL.session.add(pro)
        dbSQL.session.commit()
    return redirect(url_for('proveedores'))

@main.route('/eliminarProveedor',methods=['GET','POST'])
def eliminarProveedor():
    if request.method == 'GET':
        idProveedor = request.args.get("id")
        pro =models.Proveedor.query.get(idProveedor)
        dbSQL.session.delete(pro)
        dbSQL.session.commit()
    return redirect(url_for('proveedores'))

@main.route('/registrarUsuario',methods=['GET'])
def registrarUsuario():
    return render_template('registrarUsuario.html')

@main.route('/guardarUsuario',methods=['GET','POST'])
def guardarUsuario():
    if request.method=='POST':
        # print(request.form.get("txtEmpresa"))
        use=models.User(
            name=request.form.get("txtNombre"),
            email=request.form.get("txtCorreo"),
            password=request.form.get("txtPassword"),
            roles=request.form.get("roles"))
        dbSQL.session.add(use)
        dbSQL.session.commit()
    return render_template('usuario.html')

@main.route('/eliminarUsuario',methods=['GET','POST'])
def eliminarUsuario():
    if request.method == 'GET':
        id = request.args.get("id")
        use =models.User.query.get(id)
        dbSQL.session.delete(use)
        dbSQL.session.commit()
    return redirect(url_for('usuario'))

@main.route("/modificarUsuario",methods=['POST','GET'])
def modificarUsuario():
    if request.method == 'GET':
        id = request.args.get("id")
        user = db.session.query(Alumnos).filter(Alumnos.id == id).first()
        return render_template("modificar.html", alumno=alum)
    if request.method == 'POST':
        id = request.form.get("id")
        alum = db.session.query(Alumnos).filter(Alumnos.id==id).first()
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
