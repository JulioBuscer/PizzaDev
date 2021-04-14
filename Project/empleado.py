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

# ----------------------------- RECETARIO CRUD --------------------------------------------------
@empleado.route('/recetario')
def recetario():
    if current_user.has_role('empleado'):
        empleado = True
        query="SELECT r.idRecetario, r.nombre, r.costo, r.descripcion,r.foto, rm.cantidad,  GROUP_CONCAT(DISTINCT mp.nombre) as nombreIngre FROM recetario r LEFT JOIN recetario_materiaprima rm ON(r.idRecetario= rm.idRecetario) LEFT JOIN materiaprima mp ON(mp.idMateriaPrima= rm.idMateriaPrima) WHERE r.active=1 GROUP BY r.nombre;"
        recetario = dbSQL.session.execute(query)
        pizzasactiv = []
        for x in recetario:
            pizzasactiv.append({
                "id":x.idRecetario,
                "nombre":x.nombre,
                "costo":x.costo,
                "descripcion":x.descripcion,
                "foto":x.foto,
                "ingrediente":x.nombreIngre,
                "cantidad":x.cantidad
                })

        query2="SELECT r.idRecetario, r.nombre, r.costo, r.descripcion,r.foto, rm.cantidad,  GROUP_CONCAT(DISTINCT mp.nombre) as nombreIngre FROM recetario r LEFT JOIN recetario_materiaprima rm ON(r.idRecetario= rm.idRecetario) LEFT JOIN materiaprima mp ON(mp.idMateriaPrima= rm.idMateriaPrima) WHERE r.active=0 GROUP BY r.nombre;"
        recetario2 = dbSQL.session.execute(query2)
        pizzasdeactiv = []
        for x in recetario2:
            pizzasdeactiv.append({
                "id":x.idRecetario,
                "nombre":x.nombre,
                "costo":x.costo,
                "descripcion":x.descripcion,
                "foto":x.foto,
                "ingrediente":x.nombreIngre,
                 "cantidad":x.cantidad
                })
            
        ingre = dbSQL.session.execute("select * from materiaprima where categoria= 'materia prima';")
        
        ingredientes = []
        for x in ingre:
            ingredientes.append({
                "id":x.idMateriaPrima,
                "nombre":x.nombre,
                "descripcion":x.descripcion,
                "categoria":x.categoria,
                "precio":x.precio,
                "cantidad": x.cantidad,
                "fecha":x.fecha,
                "idProvedor":x.idProveedor
                })
        flash('Estás en recetario')
        return render_template("/empleado/administracionRecetario.html", recetario=pizzasactiv, recetariodesac= pizzasdeactiv, empleado=empleado, ingredientes=ingredientes)
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))
    
@empleado.route('/activarPizza', methods=['GET', 'POST'])
def activarPizza():
    if current_user.has_role('empleado'):
        empleado = True
        if request.method == 'GET':
            id = request.args.get("id")
            rec = dbSQL.session.query(models.Recetario).filter(
                models.Recetario.idRecetario == id).first()
        rec.active = 1
        dbSQL.session.add(rec)
        dbSQL.session.commit()
        return redirect(url_for('empleado.recetario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('/desactivarPizza', methods=['GET', 'POST'])
def eliminarPizza():
    if current_user.has_role('empleado'):
        empleado = True
        if request.method == 'GET':
            id = request.args.get("id")
            rec = dbSQL.session.query(models.Recetario).filter(
                models.Recetario.idRecetario == id).first()
        rec.active = 0
        dbSQL.session.add(rec)
        dbSQL.session.commit()
        return redirect(url_for('empleado.recetario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('updateRecetario', methods=['POST', 'GET'])
def updateRecetario():
    if current_user.has_role('empleado'):
        empleado = True
    if request.method == 'POST' :
        id = request.form.get("idRecetarioModal")
        recetario = dbSQL.session.query(models.Recetario).filter(models.Recetario.idRecetario == id).first()
        recetario.nombre = request.form.get("nombreModal")
        recetario.descripcion=request.form.get("descripcionModal")
        recetario.costo=request.form.get("costoModal")
        recetario.foto= (request.form.get("textareaModal"))

        dbSQL.session.add(recetario)
        dbSQL.session.commit()
        return redirect(url_for('empleado.recetario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('/agregarRecetario', methods=['POST', 'GET'])
def agregarRecetario():
    if current_user.has_role('empleado'):
        empleado = True 
        if request.method == 'POST':
            pizza = models.Recetario(
                nombre= request.form.get('nombrePizza'),
                descripcion= request.form.get('descripcionPizza'),
                costo= request.form.get('costoPizza'),
                 foto = (request.form.get("textarea")),
                active= 1
            )
            dbSQL.session.add(pizza)
            dbSQL.session.commit()
            lastid = dbSQL.session.query(models.Recetario).order_by(models.Recetario.idRecetario.desc()).first()
            ingredientes=request.form.getlist("ingredientes")
            for x in ingredientes:
                print("ingrediente"+x[0])
                rec_mat= "insert into recetario_materiaprima() values("+str(lastid.idRecetario)+","+x[0]+ "," + str(150) +")"
                dbSQL.session.execute(rec_mat)
                dbSQL.session.commit()
            return redirect(url_for('empleado.recetario'))
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

# ------------------------------ FIN RECETARIO CRUD -------------------------------------