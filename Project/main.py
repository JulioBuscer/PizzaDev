
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
from . import dbSQL #dbMongo
from . import models
from . models import User
from . models import Persona
from flask_principal import Principal, Permission, RoleNeed

main = Blueprint('main', __name__)


@main.route('/perfil',methods=['GET','POST'])
def perfil():
        
    if current_user.has_role('cliente'):
        cliente = True
        per = Persona()
        
        id=current_user.id
        user_=User.query.get(id)
        print('-------------'+str(id))
        
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        apellidoP= ''
        per=0
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            apellidoP=d.Persona.apellidoP
            print ('--------------aksnkj'+str(apellidoP))
        
        if apellidoP == '':
            persona= Persona(
                nombre=current_user.name,
                apellidoP = '',
                apellidoM = '',
                telefono = '',
                fotografia = '',
                idUsuario=current_user.id
            )
            dbSQL.session.add(persona)
            dbSQL.session.commit()
        
        if request.form.get("btnActualizarDatos"):
            user_.name=request.form.get('txtNombre') 
            user_.email=request.form.get('txtEmail')
            #user_.password=request.form.get('txtContrasena')
                            
            per.nombre=request.form.get('txtNombre')
            per.apellidoP=request.form.get('txtApellidoP')
            per.apellidoM=request.form.get('txtApellidoM')
            per.telefono=request.form.get('txtTelefono')
            per.fotografia=request.form.get('txtFoto')
            #dato.Persona.idUsuario=current_user.id
            
            dbSQL.session.add(user_)
            dbSQL.session.add(per)
            dbSQL.session.commit()
            
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        
        return render_template('perfil.html', cliente=cliente,name=current_user.name,user=user,user_=user_)
    
    if current_user.has_role('admin'):  
        admin = True
        
        id=current_user.id
        user_=User.query.get(id)
        print(str('--------------')+str(id))  
        
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        
        apellidoP= ''
        per=0
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            apellidoP=d.Persona.apellidoP
            print ('--------------aksnkj'+str(apellidoP))
        
        if apellidoP == '':
            persona= Persona(
                nombre=current_user.name,
                apellidoP = '',
                apellidoM = '',
                telefono = '',
                fotografia = '',
                idUsuario=current_user.id
            )
            dbSQL.session.add(persona)
            dbSQL.session.commit()
        
        if request.form.get("btnActualizarDatos"):
            user_.name=request.form.get('txtNombre') 
            user_.email=request.form.get('txtEmail')
            #user_.password=request.form.get('txtContrasena')
                            
            per.nombre=request.form.get('txtNombre')
            per.apellidoP=request.form.get('txtApellidoP')
            per.apellidoM=request.form.get('txtApellidoM')
            per.telefono=request.form.get('txtTelefono')
            per.fotografia=request.form.get('txtFoto')
            #dato.Persona.idUsuario=current_user.id
            
            dbSQL.session.add(user_)
            dbSQL.session.add(per)
            dbSQL.session.commit()
        
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        return render_template('perfil.html', admin=admin,name=current_user.name,user=user,user_=user_)
    return redirect(url_for('main.index'))

@main.route('/pedidosDia')
def pedidosDia():
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('pedidosDia.html', cliente=cliente,name=current_user.name)
    return redirect(url_for('main.index'))

@main.route('/pedidosSemana')
def pedidosSemana():
    if current_user.has_role('cliente'):
        cliente = True
        return render_template('pedidosSemana.html', cliente=cliente,name=current_user.name)
    return redirect(url_for('main.index'))

    
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


@main.route('/recetario')
def recetario():
    return render_template("recetario.html")


@main.route('/registroRecetario')
def registroRecetario():
    return render_template("registrarRecetario.html")

