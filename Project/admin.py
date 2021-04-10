from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_principal import Principal, Permission, RoleNeed
from flask_security import login_required, current_user
from flask_sqlalchemy import model
from sqlalchemy.sql.operators import match_op
from sqlalchemy.orm import joinedload
from werkzeug.utils import redirect
from . import models
from . import dbSQL


from datetime import datetime

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
    matPrima = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 1)
    #persona = dbSQL.session.query(models.users_roles,models.User, models.Role).join(models.User,models.User.id==models.Role.id).all()
    #direccion = dbSQL.session.query(models.Direccion).join(persona, persona.idDireccion == models.Direccion.idDireccion).filter(idPersona=persona)
    # matPrima = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 1)
    # matPrimaIn = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 0)
    # proveedor = dbSQL.session.query(models.Proveedor).filter(models.Proveedor.active == 1)
    #persona = dbSQL.session.query(models.Persona,models.PersonaDireccion, models.Direccion).join(models.PersonaDireccion.persona, models.PersonaDireccion.direccion).filter(models.Persona.idPersona == 2)
    #direccion = dbSQL.session.query(models.Direccion).join(persona, persona.idDireccion == models.Direccion.idDireccion).filter(idPersona=persona)
    # persona = dbSQL.session.query(models.User, models.Role).join(models.User,models.User.id==models.Role.id).all()
    # print(persona)
    # for x in persona:
    #     print(x.User.__dict__)
    #     print(x.Role.__dict__)
    if current_user.has_role('admin'):
        admin = True
        return render_template('/admin/inventario.html', admin=admin, matPr = matPrima)
    return redirect(url_for('main.index'))



@admin.route('/recetario')
def recetario():
    if current_user.has_role('admin'):
        admin = True
        query="SELECT r.idRecetario, r.nombre, r.costo, r.descripcion,r.foto,  GROUP_CONCAT(DISTINCT mp.nombre) as nombreIngre FROM recetario r LEFT JOIN recetario_materiaprima rm ON(r.idRecetario= rm.idRecetario) LEFT JOIN materiaprima mp ON(mp.idMateriaPrima= rm.idMateriaPrima) WHERE r.active=1 GROUP BY r.nombre;"
    
        recetario = dbSQL.session.execute(query)
        pizzasactiv = []
        for x in recetario:
            pizzasactiv.append({
                "id":x.idRecetario,
                "nombre":x.nombre,
                "costo":x.costo,
                "descripcion":x.descripcion,
                "foto":x.foto,
                "ingrediente":x.nombreIngre
                })
            
            
        query2="SELECT r.idRecetario, r.nombre, r.costo, r.descripcion,r.foto,  GROUP_CONCAT(DISTINCT mp.nombre) as nombreIngre FROM recetario r LEFT JOIN recetario_materiaprima rm ON(r.idRecetario= rm.idRecetario) LEFT JOIN materiaprima mp ON(mp.idMateriaPrima= rm.idMateriaPrima) WHERE r.active=0 GROUP BY r.nombre;"
        
        recetario2 = dbSQL.session.execute(query2)
        pizzasdeactiv = []
        for x in recetario2:
            pizzasdeactiv.append({
                "id":x.idRecetario,
                "nombre":x.nombre,
                "costo":x.costo,
                "descripcion":x.descripcion,
                "foto":x.foto,
                "ingrediente":x.nombreIngre
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
            
        
        return render_template("AdministracionRecetario.html", recetario=pizzasactiv, recetariodesac= pizzasdeactiv, admin=admin, ingredientes=ingredientes)
    return redirect(url_for('main.index'))
            
        
   

@admin.route('/activarPizza', methods=['GET', 'POST'])
def activarPizza():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("id")
            rec = dbSQL.session.query(models.Recetario).filter(
                models.Recetario.idRecetario == id).first()
        rec.active = 1
        dbSQL.session.add(rec)
        dbSQL.session.commit()
        return redirect(url_for('admin.recetario'))
    return redirect(url_for('main.index'))

@admin.route('/desactivarPizza', methods=['GET', 'POST'])
def eliminarPizza():
    if current_user.has_role('admin'):
        admin = True
        if request.method == 'GET':
            id = request.args.get("id")
            rec = dbSQL.session.query(models.Recetario).filter(
                models.Recetario.idRecetario == id).first()
        rec.active = 0
        dbSQL.session.add(rec)
        dbSQL.session.commit()
        return redirect(url_for('admin.recetario'))
    return redirect(url_for('main.index'))





@admin.route('updateRecetario', methods=['POST', 'GET'])
def updateRecetario():
    if current_user.has_role('admin'):
        admin = True
    if request.method == 'POST' :
        id = request.form.get("idRecetarioModal")
        print(id)
        recetario = dbSQL.session.query(models.Recetario).filter(models.Recetario.idRecetario == id).first()
        recetario.nombre = request.form.get("nombreModal")
        recetario.descripcion=request.form.get("descripcionModal")
        recetario.costo=request.form.get("costoModal")
        recetario.foto= ("data:image/jpeg;base64,"+request.form.get("textareaModal"))

        dbSQL.session.add(recetario)
        dbSQL.session.commit()
        return redirect(url_for('admin.recetario'))
    return redirect(url_for('main.index'))

@admin.route('/agregarRecetario', methods=['POST', 'GET'])
def agregarRecetario():
    if current_user.has_role('admin'):
        admin = True 
        if request.method == 'POST':
            pizza = models.Recetario(
                nombre= request.form.get('nombrePizza'),
                descripcion= request.form.get('descripcionPizza'),
                costo= request.form.get('costoPizza'),
                 foto = ("data:image/jpeg;base64,"+request.form.get("textarea")),
                active= 1
                     
            )
            dbSQL.session.add(pizza)
            dbSQL.session.commit()
            
            
            lastid = dbSQL.session.query(models.Recetario).order_by(models.Recetario.idRecetario.desc()).first()
            
            ingredientes=request.form.getlist("ingredientes")
            print(ingredientes)
            for x in ingredientes:
                print("ingrediente"+x[0])
                rec_mat= "insert into recetario_materiaprima() values("+str(lastid.idRecetario)+","+x[0]+ "," + str(0) +")"
                dbSQL.session.execute(rec_mat)
                dbSQL.session.commit()
        
            
            
            return redirect(url_for('admin.recetario'))
    return redirect(url_for('main.index'))







@admin.route('deleteMatPrim')
def deleteMatPrim():
    if current_user.has_role('admin'):
        admins = True
    if request.method == 'GET':
        id = request.args.get("id")
        matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
        matPrim.nombre = request.args.get("name")
        matPrim.descripcion= request.args.get("descripcion")
        matPrim.categoria = request.args.get("categoria")
        matPrim.precio = request.args.get("precio")
        matPrim.cantidad = request.args.get("cantidad")
        matPrim.fecha = str(datetime.now())
        matPrim.active = bool(False)
        matPrim.idProveedor = request.args.get("proveedor_empresa")
        dbSQL.session.add(matPrim)
        dbSQL.session.commit()
        return redirect(url_for('admin.inventario'))

@admin.route('updateMatPrim')
def updateMatPrim():
    if current_user.has_role('admin'):
        admins = True
    if request.method == 'GET':
        id = request.args.get("id")
        matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
        matPrim.nombre = request.args.get("name")
        matPrim.descripcion= request.args.get("descripcion")
        matPrim.categoria = request.args.get("categoria")
        matPrim.precio = request.args.get("precio")
        matPrim.cantidad = request.args.get("cantidad")
        matPrim.fecha = str(datetime.now())
        matPrim.active = bool(True)
        matPrim.idProveedor = request.args.get("proveedor_empresa")
        dbSQL.session.add(matPrim)
        dbSQL.session.commit()
        return redirect(url_for('admin.inventario'))
