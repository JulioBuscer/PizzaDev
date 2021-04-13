from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_security import current_user
from flask_security.decorators import roles_required
from werkzeug.utils import redirect
from . import models
from . import dbSQL

from datetime import date, datetime
empleado = Blueprint('empleado', __name__, url_prefix='/empleado')

# ----------------------------- MATERIA PRIMA CRUD --------------------------------
@empleado.route('inventario')
@roles_required('empleado')
def inventario():
    #persona = dbSQL.session.query(models.Persona,models.PersonaDireccion, models.Direccion).join(models.PersonaDireccion.persona, models.PersonaDireccion.direccion).filter(models.Persona.idPersona == 2)
    #direccion = dbSQL.session.query(models.Direccion).join(persona, persona.idDireccion == models.Direccion.idDireccion).filter(idPersona=persona)
    #persona = dbSQL.session.query(models.users_roles, models.User, models.Role).join(models.User).join(models.Role).all()
    #for x in persona:
    #    print(x)
    if current_user.has_role('empleado'):
        empleado = True
        matPrima = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 1)
        matPrimaIn = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 0)
        proveedor = dbSQL.session.query(models.Proveedor).filter(models.Proveedor.active == 1)
        flash('Estás en inventario de materia prima')
        return render_template('/empleado/inventario.html', name=current_user.name, empleado=empleado, matPr = matPrima, matPrIn = matPrimaIn, prov= proveedor)
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('deleteMatPrim')
@roles_required('empleado')
def deleteMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            id = request.args.get("id")
            matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
            matPrim.nombre = request.args.get("name")
            matPrim.descripcion= request.args.get("descripcion")
            matPrim.categoria = request.args.get("categoria")
            matPrim.precio = request.args.get("precio")
            matPrim.cantidad = request.args.get("cantidad")
            matPrim.fecha = str(datetime.today())
            matPrim.active = bool(False)
            matPrim.idProveedor = request.args.get("proveedor_empresa")
            dbSQL.session.add(matPrim)
            matPrim.unidad = request.args.get("unidad")
            dbSQL.session.commit()
            flash('Materia prima eliminada')
            return redirect(url_for('empleado.inventario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('updateMatPrim')
@roles_required('empleado')
def updateMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            id = request.args.get("id")
            matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
            matPrim.nombre = request.args.get("name")
            matPrim.descripcion= request.args.get("descripcion")
            matPrim.categoria = request.args.get("categoria")
            matPrim.precio = request.args.get("precio")
            matPrim.cantidad = request.args.get("cantidad")
            matPrim.fecha = str(datetime.today())
            matPrim.active = bool(True)
            matPrim.idProveedor = request.args.get("proveedor_empresa")
            matPrim.unidad = request.args.get("unidad")
            dbSQL.session.add(matPrim)
            dbSQL.session.commit()
            flash('Materia prima actualizada')
            return redirect(url_for('empleado.inventario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('insertMatPrim')
@roles_required('empleado')
def insertMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            matPrim = models.MateriaPrima(nombre=request.args.get("name"),
                     descripcion=request.args.get("descripcion"),
                     categoria=request.args.get("categoria"),
                     precio=request.args.get("precio"),
                     cantidad=request.args.get("cantidad"),
                     fecha=str(datetime.today()),
                     unidad=request.args.get("unidad"),
                     active = bool(True),
                     idProveedor=request.args.get("proveedor_empresa"))
                     
            dbSQL.session.add(matPrim)
            dbSQL.session.commit()
            flash('Materia prima actualizada')
            return redirect(url_for('empleado.inventario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

# ------------------------------ FIN MATERIA PRIMA CRUD -----------------------------------------