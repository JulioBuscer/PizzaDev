from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_principal import Principal, Permission, RoleNeed
from flask_security import login_required, current_user
from werkzeug.utils import redirect

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
