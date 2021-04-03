from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_principal import Principal, Permission, RoleNeed
from flask_security import login_required, current_user
from sqlalchemy.sql.operators import match_op
from sqlalchemy.orm import joinedload
from werkzeug.utils import redirect
from . import models
from . import dbSQL
admin = Blueprint('admin', __name__, url_prefix='/admin')


@admin.route('ventas')
def ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/ventas.html', admin=admin)
    return redirect(url_for('main.index'))

@admin.route('detalle_venta')
def detalle_ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/detalle_venta.html', admin=admin)
    return redirect(url_for('main.index'))

@admin.route('inventario')
def inventario():
    matPrima = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).all()
    matPrima = []
    persona = dbSQL.session.query(models.Persona,models.PersonaDireccion, models.Direccion).join(models.PersonaDireccion.persona, models.PersonaDireccion.direccion).filter(models.Persona.idPersona == 2)
    #direccion = dbSQL.session.query(models.Direccion).join(persona, persona.idDireccion == models.Direccion.idDireccion).filter(idPersona=persona)
    print(persona)
    for x in persona:
        print(x.Persona.__dict__)
        print(x.PersonaDireccion.__dict__)
        print(x.Direccion.__dict__)
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/inventario.html', admin=admin, matPr = matPrima)
    return redirect(url_for('main.index'))