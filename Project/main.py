# import datetime module
import datetime
from operator import concat
from flask import Blueprint, render_template, request, flash
from flask.helpers import url_for
from flask_security import current_user
from werkzeug.utils import redirect
from . import dbSQL #dbMongo
from . import models
from . models import User
from . models import Persona
from . models import Direccion
from . models import personas_direcciones
import shortuuid

main = Blueprint('main', __name__)
arregloDir = []
arreglo_ventas_per = []
arregloDetalle = []
arregloAll =[]

@main.route('/perfil',methods=['GET','POST'])
def perfil():
    if current_user.has_role('empleado'):
        empleado = True
        admin = True
        arregloDir.clear()
        #Inserción y actualización de datos 
        cliente = True
        
        per = Persona()
        
        id=current_user.id
        user_=User.query.get(id)

        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        print(user)
        apellidoP= ''
        per=0
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            apellidoP=d.Persona.apellidoP
        
        if apellidoP == '':
            persona= Persona(
                nombre=current_user.name,
                apellidoP = '-',
                apellidoM = '-',
                telefono = '-',
                fotografia = '-',
                idUsuario=current_user.id
            )
            print('print'+str(current_user.id))
            dbSQL.session.add(persona)
            dbSQL.session.commit()
        
        else:
            user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id)                 
        query = 'select d.idDireccion,d.calle,d.colonia,d.numeroInt,d.numeroExt,d.codigoPostal,d.descripcion from personas_direcciones pd inner join persona p on pd.idPersona = p.idPersona inner join direccion d on pd.idDireccion = d.idDireccion inner join user u on p.idUsuario = u.id where u.id = '+ str(id) +' ;'
            
        direcciones= dbSQL.session.execute(query)
        for x in direcciones:
            arregloDir.append({
                "id":x.idDireccion,
                "calle": x.calle,
                "colonia": x.colonia,
                "numInt": x.numeroInt,
                "numExt": x.numeroExt,
                "cp": x.codigoPostal,
                "descripcion": x.descripcion
            })
        return render_template('perfil.html', empleado=empleado,name=current_user.name,user=user,user_=user_, direcciones=arregloDir)
    if current_user.has_role('admin'):
        admin = True
        arregloDir.clear()
        #Inserción y actualización de datos 
        cliente = True
        
        per = Persona()
        
        id=current_user.id
        user_=User.query.get(id)

        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        print(user)
        apellidoP= ''
        per=0
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            apellidoP=d.Persona.apellidoP
        
        if apellidoP == '':
            persona= Persona(
                nombre=current_user.name,
                apellidoP = '-',
                apellidoM = '-',
                telefono = '-',
                fotografia = '-',
                idUsuario=current_user.id
            )
            print('print'+str(current_user.id))
            dbSQL.session.add(persona)
            dbSQL.session.commit()
        
        else:
            user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id)                 
        query = 'select d.idDireccion,d.calle,d.colonia,d.numeroInt,d.numeroExt,d.codigoPostal,d.descripcion from personas_direcciones pd inner join persona p on pd.idPersona = p.idPersona inner join direccion d on pd.idDireccion = d.idDireccion inner join user u on p.idUsuario = u.id where u.id = '+ str(id) +' ;'
            
        direcciones= dbSQL.session.execute(query)
        for x in direcciones:
            arregloDir.append({
                "id":x.idDireccion,
                "calle": x.calle,
                "colonia": x.colonia,
                "numInt": x.numeroInt,
                "numExt": x.numeroExt,
                "cp": x.codigoPostal,
                "descripcion": x.descripcion
            })
        return render_template('perfil.html', admin=admin,name=current_user.name,user=user,user_=user_, direcciones=arregloDir)
    if current_user.has_role('cliente'):
        arregloDir.clear()
        #Inserción y actualización de datos 
        cliente = True
        
        per = Persona()
        
        id=current_user.id
        user_=User.query.get(id)

        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        print(user)
        apellidoP= ''
        per=0
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            apellidoP=d.Persona.apellidoP
        
        if apellidoP == '':
            persona= Persona(
                nombre=current_user.name,
                apellidoP = '-',
                apellidoM = '-',
                telefono = '-',
                fotografia = '-',
                idUsuario=current_user.id
            )
            print('print'+str(current_user.id))
            dbSQL.session.add(persona)
            dbSQL.session.commit()
        
        else:
            user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id)                 
        query = 'select d.idDireccion,d.calle,d.colonia,d.numeroInt,d.numeroExt,d.codigoPostal,d.descripcion from personas_direcciones pd inner join persona p on pd.idPersona = p.idPersona inner join direccion d on pd.idDireccion = d.idDireccion inner join user u on p.idUsuario = u.id where u.id = '+ str(id) +' ;'
            
        direcciones= dbSQL.session.execute(query)
        for x in direcciones:
            arregloDir.append({
                "id":x.idDireccion,
                "calle": x.calle,
                "colonia": x.colonia,
                "numInt": x.numeroInt,
                "numExt": x.numeroExt,
                "cp": x.codigoPostal,
                "descripcion": x.descripcion
            })
        return render_template('perfil.html', cliente=cliente,name=current_user.name,user=user,user_=user_, direcciones=arregloDir)
    return redirect(url_for('main.index'))

@main.route('/agregarDatos',methods=['GET','POST'])
def agregarDatos():
    
    if current_user.has_role('cliente') or current_user.has_role('empleado') or current_user.has_role('admin'):
        
        cliente = True
        
        id=current_user.id
        user_=User.query.get(id)
        print('-------------'+str(id))
        #per=0
        
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
        
        user_.name=request.form.get('txtNombre') 
        user_.email=request.form.get('txtEmail')            

        per.nombre=request.form.get('txtNombre')
        per.apellidoP=request.form.get('txtApellidoP')
        per.apellidoM=request.form.get('txtApellidoM')
        per.telefono=request.form.get('txtTelefono')
        per.fotografia=request.form.get('textarea')
        #dato.Persona.idUsuario=current_user.id
            
        dbSQL.session.add(user_)
        dbSQL.session.add(per)
        dbSQL.session.commit()
        
        arregloDir.clear()
        
        return redirect('/perfil')
    return redirect(url_for('main.index'))
    
@main.route('/eliminarDireccion')
def eliminarDireccion():
    if current_user.has_role('admin'):
        admin = True
        #id=current_user.id
        direccion = Direccion()
        id = request.args.get("id")
        direccion= Direccion.query.get(id)
        dbSQL.session.delete(direccion)
        dbSQL.session.commit()
        
        arregloDir.clear()
        
        return redirect('/perfil')
        
        #return render_template('perfil.html', admin=admin, name=current_user.name,direcciones=direcciones,user=user)
    
    if current_user.has_role('cliente'):
        cliente = True
        #id=current_user.id
        
        direccion = Direccion()
        id = request.args.get("id")
        direccion= Direccion.query.get(id)
        dbSQL.session.delete(direccion)
        dbSQL.session.commit()
        
        arregloDir.clear()
        
        return redirect('/perfil')
    
    return redirect(url_for('main.index'))

@main.route('/agregarDirección',methods=['GET','POST'])
def agregarDireccion():
    if current_user.has_role('cliente'):
        cliente = True
        
        id=current_user.id
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
        
        insercion= False
        dir= Direccion(
            calle=request.form.get('txtCalle'),
            colonia = request.form.get('txtColonia'),
            numeroInt = request.form.get('txtNumInt'),
            numeroExt = request.form.get('txtNumExt'),
            codigoPostal = request.form.get('txtCP'),
            descripcion = request.form.get('txtDescripcion'))
        dbSQL.session.add(dir)
        dbSQL.session.commit()
            
        insercion= True
        if insercion:
            lastid = dbSQL.session.query(Direccion).order_by(Direccion.idDireccion.desc()).first()
            per_dir= personas_direcciones.insert().values(idPersona=per.idPersona,idDireccion=(lastid.idDireccion))
            dbSQL.session.execute(per_dir)
            dbSQL.session.commit()
            
            arregloDir.clear()
        
            return redirect('/perfil')
    
    if current_user.has_role('admin'):
        admin = True
        
        id=current_user.id
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
        
        insercion= False
        dir= Direccion(
            calle=request.form.get('txtCalle'),
            colonia = request.form.get('txtColonia'),
            numeroInt = request.form.get('txtNumInt'),
            numeroExt = request.form.get('txtNumExt'),
            codigoPostal = request.form.get('txtCP'),
            descripcion = request.form.get('txtDescripcion'))
        dbSQL.session.add(dir)
        dbSQL.session.commit()
            
        insercion= True
        if insercion:
            lastid = dbSQL.session.query(Direccion).order_by(Direccion.idDireccion.desc()).first()
            per_dir= personas_direcciones.insert().values(idPersona=per.idPersona,idDireccion=(lastid.idDireccion))
            dbSQL.session.execute(per_dir)
            dbSQL.session.commit()
            
            arregloDir.clear()

            return redirect('/perfil')
    return redirect(url_for('main.index'))

@main.route('/modificarDirección')
def modificarDireccion():
    if current_user.has_role('admin'):
        admin = True
        
        #per=Persona.query.get(d.Persona.idPersona)
        id = request.args.get("id")
        print(request.args.get("colonia"))
        dir=dbSQL.session.query(Direccion).filter(Direccion.idDireccion==id).first()
        
        dir.calle =request.args.get("calle")
        dir.colonia =request.args.get("colonia")
        dir.numeroInt =request.args.get("numeroInt")
        dir.numeroExt =request.args.get("numeroExt")
        dir.codigoPostal = request.args.get("cp")
        dir.descripcion = request.args.get("descripcion")
            
        dbSQL.session.add(dir)
        dbSQL.session.commit()
        
        arregloDir.clear()
        
        return redirect('/perfil')
        
    
    if current_user.has_role('cliente'):
        cliente = True
        
        #per=Persona.query.get(d.Persona.idPersona)
        id = request.args.get("id")
        print(request.args.get("colonia"))
        dir=dbSQL.session.query(Direccion).filter(Direccion.idDireccion==id).first()
        
        dir.calle =request.args.get("calle")
        dir.colonia =request.args.get("colonia")
        dir.numeroInt =request.args.get("numeroInt")
        dir.numeroExt =request.args.get("numeroExt")
        dir.codigoPostal = request.args.get("cp")
        dir.descripcion = request.args.get("descripcion")
            
        dbSQL.session.add(dir)
        dbSQL.session.commit()
        
        arregloDir.clear()
        
        return redirect('/perfil')
        
    return redirect(url_for('main.index'))

@main.route('/pedidos',methods=['GET','POST'])
def pedidos():
    if current_user.has_role('cliente'):
        cliente = True
        
        arreglo_ventas_per.clear()
        arregloDetalle.clear()
        
        id=current_user.id
        user = dbSQL.session.query(models.Persona,models.User).join(models.User, models.Persona.idUsuario == models.User.id).filter(models.Persona.idUsuario==id) 
        for d in user:
            per=Persona.query.get(d.Persona.idPersona)
            idPersona = d.Persona.idPersona
        
        query = 'select r.nombre, v.cantidad, v.subtotal, r.costo, v.fecha,v.idVenta from venta_recetario vr inner join venta v on vr.idVenta = v.idVenta inner join recetario r on vr.idRecetario = r.idRecetario where v.idPersona = '+ str(idPersona) +';'       
        ventas_persona= dbSQL.session.execute(query)
              
        for x in ventas_persona:
            
            arreglo_ventas_per.append({
                "id":str(shortuuid.uuid()),
                "fecha": x.fecha,
                "sabor":x.nombre,
                "cantidad":x.cantidad,
                "costo":x.costo,
                "subtotal":x.subtotal
            })
            
            print ('ventas'+str(arreglo_ventas_per))  
        return render_template('pedidos.html', cliente=cliente,name=current_user.name,arreglo_ventas_per=arreglo_ventas_per)
    return redirect(url_for('main.index'))

# -------------------- INICIO ----------------------
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

# ----------------------- PENDIENTE ------------------------
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

# ------------------------ MENU CLIENTE -----------------------
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
