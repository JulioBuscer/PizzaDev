from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_security import current_user
from flask_security.decorators import roles_required
from werkzeug.utils import redirect
from werkzeug.security import generate_password_hash
from . import models
from . import dbSQL, userDataStore

from datetime import datetime

admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('ventas')
@roles_required('admin')
def ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/ventas.html', admin=admin)
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))


@admin.route('detalle_venta')
@roles_required('admin')
def detalle_ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/detalle_venta.html', admin=admin)
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

# --------------------------------- CRUD USUARIO --------------------------------------


@admin.route("/usuario")
def usuario():
    if current_user.has_role('admin'):
        admin = True
        try:
            roles = models.Role.query.all()
            usuariorole = dbSQL.session.query(models.users_roles, models.User, models.Role).join(
                models.User).join(models.Role).filter(models.User.active == 1)
            usuariorole1 = dbSQL.session.query(models.users_roles, models.User, models.Role).join(
                models.User).join(models.Role).filter(models.User.active == 0)
            flash("Estás en usuario")
            return render_template("admin/usuario.html", usuarios=usuariorole, usuarios1=usuariorole1, roles=roles, admin=admin)
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))


@admin.route("/modificarUsuario", methods=['POST', 'GET'])
def modificarUsuario():
    if current_user.has_role('admin'):
        admin = True
        try:
            if request.method == 'GET':
                id = request.args.get("id1")
                usu = dbSQL.session.query(models.User).filter(
                    models.User.id == id).first()

                usu.email = request.args.get("txtCorreo1")
                usu.password = generate_password_hash(
                    request.args.get("txtContraseña1"), method='sha256')
                usu.name = request.args.get("txtNombre1")
                r = request.args.get("cmbRol1")
                if r == "admin":
                    rol = 1
                elif r == "cliente":
                    rol = 2
                else:
                    rol = 3
                dbSQL.session.add(usu)
                dbSQL.session.commit()
                queryR = 'update users_roles set roleId=' + \
                    str(rol)+' where userId='+str(id)+' ;'
                dbSQL.session.execute(queryR)
                dbSQL.session.commit()
            flash("Usuario modificado")
            return redirect(url_for('admin.usuario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

    # query1='update user set name='+str(usu.User.name+', email='+usu.User.email+', password='+usu.User.password+' where id='+str(id)+';'
    # dbSQL.session.execute(query1)


@admin.route('/activarrUsuario', methods=['GET', 'POST'])
def activarrUsuario():
    if current_user.has_role('admin'):
        admin = True
        try:
            if request.method == 'GET':
                id = request.args.get("id")
                user = dbSQL.session.query(models.User).filter(
                    models.User.id == id).first()
            user.active = 1
            dbSQL.session.add(user)
            dbSQL.session.commit()
            flash("Usuario activado")
            return redirect(url_for('admin.usuario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')

    return redirect(url_for('main.index'))


@admin.route('/eliminarUsuario', methods=['GET', 'POST'])
def eliminarUsuario():
    if current_user.has_role('admin'):
        admin = True
        try:
            if request.method == 'GET':
                id = request.args.get("id")
                user = dbSQL.session.query(models.User).filter(
                    models.User.id == id).first()
            user.active = 0
            dbSQL.session.add(user)
            dbSQL.session.commit()
            flash("Usuario eliminado")
            return redirect(url_for('admin.usuario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))


@ admin.route('/guardarUsuario', methods=['GET', 'POST'])
def guardarUsuario():
    if current_user.has_role('admin'):
        admin = True
        try:
            if request.method == 'POST':
                name = request.form.get("txtNombre")
                email = request.form.get("txtCorreo")
                password = request.form.get("txtContraseña")
                roles = request.form.get("cmbRol")

                usu = models.User.query.filter_by(email=email).first()

                if roles == "cliente":
                    print("entro")
                    cliente_role = userDataStore.find_or_create_role('cliente')
                    print(cliente_role)
                    userDataStore.create_user(name=name, email=email,
                                              password=generate_password_hash(password, method='sha256'), roles=[cliente_role])
                    # Agregamos el usuario a la bd.
                    dbSQL.session.commit()
                elif roles == 'admin':
                    admin_role = userDataStore.find_or_create_role('admin')
                    print(admin_role)
                    userDataStore.create_user(name=name, email=email,
                                              password=generate_password_hash(password, method='sha256'), roles=[admin_role])
                    # Agregamos el usuario a la bd.
                    dbSQL.session.commit()
                else:
                    empleado_role = userDataStore.find_or_create_role(
                        'empleado')
                    userDataStore.create_user(name=name, email=email,
                                              password=generate_password_hash(password, method='sha256'), roles=[empleado_role])
                    # Agregamos el usuario a la bd.
                    dbSQL.session.commit()
            flash("Usuario registrado")
            return redirect(url_for('admin.usuario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

# ------------------------------- FIN CRUD USUARIO ------------------------------------
