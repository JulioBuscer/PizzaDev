
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
        return render_template('index.html', admin=admin, name=current_user.name)
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('index.html', cliente=cliente, name=current_user.name)
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
    
    contador= dbSQL.session.query(models.recetario_materiaprima).all()
    recetario = dbSQL.session.query( models.recetario_materiaprima,models.Recetario, models.MateriaPrima).join(models.Recetario).join(models.MateriaPrima).filter(models.Recetario.idRecetario==models.Recetario.idRecetario)
    print(recetario)
    conta=[]
    
    for x in recetario:
        print(x.Recetario.idRecetario)


    return render_template("menu.html", menu=recetario)


@main.route('/recetario')
def registroInventario():
    recetario = dbSQL.session.query( models.recetario_materiaprima,models.Recetario, models.MateriaPrima).join(models.Recetario).join(models.MateriaPrima).filter(models.Recetario.idRecetario==models.Recetario.idRecetario)
    
    
    return render_template("AdministracionRecetario.html", recetario=recetario)


