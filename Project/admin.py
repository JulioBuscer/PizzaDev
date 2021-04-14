from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_security import current_user
from flask_security.decorators import roles_required
from werkzeug.utils import redirect
from . import models
from . import dbSQL

from datetime import datetime

admin = Blueprint('admin', __name__, url_prefix='/admin')

@admin.route('ventas')
@roles_required('admin')
def ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/ventas.html', admin=admin)
    return redirect(url_for('main.index'))

@admin.route('detalle_venta')
@roles_required('admin')
def detalle_ventas():
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/detalle_venta.html', admin=admin)
    return redirect(url_for('main.index'))

