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

@admin.route('/recetario')
def recetario():
    if current_user.has_role('admin'):
        admin = True
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
        recetario.foto= (request.form.get("textareaModal"))

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
                 foto = (request.form.get("textarea")),
                active= 1
                     
            )
            dbSQL.session.add(pizza)
            dbSQL.session.commit()
            
            
            lastid = dbSQL.session.query(models.Recetario).order_by(models.Recetario.idRecetario.desc()).first()
            
            ingredientes=request.form.getlist("ingredientes")
            print(ingredientes)
            for x in ingredientes:
                print("ingrediente"+x[0])
                rec_mat= "insert into recetario_materiaprima() values("+str(lastid.idRecetario)+","+x[0]+ "," + str(150) +")"
                dbSQL.session.execute(rec_mat)
                dbSQL.session.commit()
        
            
            
            return redirect(url_for('admin.recetario'))
    return redirect(url_for('main.index'))

