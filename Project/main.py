# import datetime module
import datetime
from operator import concat
from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_security import current_user
from werkzeug.utils import redirect
from . import dbSQL
from . import models

main = Blueprint('main', __name__)


@main.route('/perfil')
def perfil():
    return render_template('perfil.html')


@main.route('/pedidosDia')
def pedidosDia():
    return render_template('pedidosDia.html')


@main.route('/pedidosSemana')
def pedidosSemana():
    return render_template('pedidosSemana.html')


@main.route('/')
def index():
    if current_user.has_role('admin'):
        admin = True
        return render_template('index.html', admin=admin, name=current_user.name)
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('index.html', cliente=cliente, name=current_user.name)
    if current_user.has_role('empleado'):
        empleado = True
        return render_template('index.html', empleado=empleado, name=current_user.name)
    return render_template('index.html')



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


@main.route('/menu')
def menu():
    if current_user.has_role('cliente'):
        cliente = True
        query = "SELECT r.idRecetario, r.nombre, r.costo, r.descripcion,r.foto,  GROUP_CONCAT(DISTINCT mp.nombre) as nombreIngre FROM recetario r LEFT JOIN recetario_materiaprima rm ON(r.idRecetario= rm.idRecetario) LEFT JOIN materiaprima mp ON(mp.idMateriaPrima= rm.idMateriaPrima) WHERE r.active=1 GROUP BY r.nombre;"
        recetario = dbSQL.session.execute(query)
        pizzas = []
        for x in recetario:
            pizzas.append({
                "id": x.idRecetario,
                "nombre": x.nombre,
                "costo": x.costo,
                "descripcion": x.descripcion,
                "foto": x.foto,
                "ingrediente": x.nombreIngre
            })
        return render_template('cliente/menu.html', menu=pizzas, cliente=cliente)
    flash('Debes de iniciar sesión para poder ordenar')
    return redirect(url_for('main.index'))
