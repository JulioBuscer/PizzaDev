from flask import Blueprint, render_template, redirect, url_for, request, flash
from flask_security import current_user
from flask_security.decorators import roles_required
from werkzeug.utils import redirect
from . import models
from . import dbSQL
from datetime import date
empleado = Blueprint('empleado', __name__, url_prefix='/empleado')

# ----------------------------- MATERIA PRIMA CRUD --------------------------------
@empleado.route('inventario')
@roles_required('empleado')
def inventario():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            matPrima = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 1)
            matPrimaIn = dbSQL.session.query(models.MateriaPrima).join(models.Proveedor, models.Proveedor.idProveedor == models.MateriaPrima.idProveedor).filter(models.MateriaPrima.active == 0)
            proveedor = dbSQL.session.query(models.Proveedor).filter(models.Proveedor.active == 1)
            flash('Estás en inventario de materia prima')
            return render_template('/empleado/inventario.html', name=current_user.name, empleado=empleado, matPr = matPrima, matPrIn = matPrimaIn, prov= proveedor)
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('deleteMatPrim')
@roles_required('empleado')
def deleteMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            try:
                id = request.args.get("id")
                matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
                matPrim.nombre = request.args.get("name")
                matPrim.descripcion= request.args.get("descripcion")
                matPrim.categoria = request.args.get("categoria")
                matPrim.precio = request.args.get("precio")
                matPrim.cantidad = request.args.get("cantidad")
                matPrim.fecha = str(date.today())
                matPrim.active = bool(False)
                matPrim.idProveedor = request.args.get("proveedor_empresa")
                dbSQL.session.add(matPrim)
                matPrim.unidad = request.args.get("unidad")
                dbSQL.session.commit()
                flash('Materia prima eliminada')
                return redirect(url_for('empleado.inventario'))
            except:
                flash('Ha ocurrido un error al consultar la información')
                return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('updateMatPrim')
@roles_required('empleado')
def updateMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            try:
                id = request.args.get("id")
                matPrim = dbSQL.session.query(models.MateriaPrima).filter(models.MateriaPrima.idMateriaPrima == id).first()
                matPrim.nombre = request.args.get("name")
                matPrim.descripcion= request.args.get("descripcion")
                matPrim.categoria = request.args.get("categoria")
                matPrim.precio = request.args.get("precio")
                matPrim.cantidad = request.args.get("cantidad")
                matPrim.fecha = str(date.today())
                matPrim.active = bool(True)
                matPrim.idProveedor = request.args.get("proveedor_empresa")
                matPrim.unidad = request.args.get("unidad")
                dbSQL.session.add(matPrim)
                dbSQL.session.commit()
                flash('Materia prima actualizada')
                return redirect(url_for('empleado.inventario'))
            except:
                flash('Ha ocurrido un error al consultar la información')
                return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('insertMatPrim')
@roles_required('empleado')
def insertMatPrim():
    if current_user.has_role('empleado'):
        empleados = True
        if request.method == 'GET':
            try:
                matPrim = models.MateriaPrima(nombre=request.args.get("name"),
                        descripcion=request.args.get("descripcion"),
                        categoria=request.args.get("categoria"),
                        precio=request.args.get("precio"),
                        cantidad=request.args.get("cantidad"),
                        fecha=str(date.today()),
                        unidad=request.args.get("unidad"),
                        active = bool(True),
                        idProveedor=request.args.get("proveedor_empresa"))
                        
                dbSQL.session.add(matPrim)
                dbSQL.session.commit()
                flash('Materia prima actualizada')
                return redirect(url_for('empleado.inventario'))
            except:
                flash('Ha ocurrido un error al consultar la información')
                return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

# ------------------------------ FIN MATERIA PRIMA CRUD -----------------------------------------

# ----------------------------- RECETARIO CRUD --------------------------------------------------

@empleado.route('/recetario')
@roles_required('empleado')
def recetario():
    if current_user.has_role('empleado'):
        empleado = True
        try:
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
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))
    
@empleado.route('/activarPizza', methods=['GET', 'POST'])
@roles_required('empleado')
def activarPizza():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'GET':
                id = request.args.get("id")
                rec = dbSQL.session.query(models.Recetario).filter(
                    models.Recetario.idRecetario == id).first()
            rec.active = 1
            dbSQL.session.add(rec)
            dbSQL.session.commit()
            flash("Recetario activado")
            return redirect(url_for('empleado.recetario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('/desactivarPizza', methods=['GET', 'POST'])
@roles_required('empleado')
def eliminarPizza():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'GET':
                id = request.args.get("id")
                rec = dbSQL.session.query(models.Recetario).filter(
                    models.Recetario.idRecetario == id).first()
            rec.active = 0
            dbSQL.session.add(rec)
            dbSQL.session.commit()
            flash("Recetario eliminado")
            return redirect(url_for('empleado.recetario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('updateRecetario', methods=['POST', 'GET'])
@roles_required('empleado')
def updateRecetario():
    if current_user.has_role('empleado'):
        empleado = True
    if request.method == 'POST' :
        try:
            id = request.form.get("idRecetarioModal")
            recetario = dbSQL.session.query(models.Recetario).filter(models.Recetario.idRecetario == id).first()
            recetario.nombre = request.form.get("nombreModal")
            recetario.descripcion=request.form.get("descripcionModal")
            recetario.costo=request.form.get("costoModal")
            recetario.foto= (request.form.get("textareaModal"))

            dbSQL.session.add(recetario)
            dbSQL.session.commit()
            flash("Recetario actualizado")
            return redirect(url_for('empleado.recetario'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

@empleado.route('/agregarRecetario', methods=['POST', 'GET'])
@roles_required('empleado')
def agregarRecetario():
    if current_user.has_role('empleado'):
        empleado = True 
        if request.method == 'POST':
            try:
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
                flash("Recetario registrado")
                return redirect(url_for('empleado.recetario'))
            except:
                flash('Ha ocurrido un error al consultar la información')
                return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('empleado.index'))

# ------------------------------ FIN RECETARIO CRUD -------------------------------------

# ----------------------------- PROVEEDOR CRUD ------------------------------------------
@empleado.route("/proveedores")
@roles_required('empleado')
def proveedores():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            pro = models.Proveedor.query.filter(models.Proveedor.active == 1).all()
            pro1 = models.Proveedor.query.filter(
                models.Proveedor.active == 0).all()
            flash('Estás en proveedores')
            return render_template("empleado/proveedores.html", proveedores=pro, proveedores1=pro1, empleado=empleado)
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('/guardarProveedor', methods=['GET', 'POST'])
@roles_required('empleado')
def guardarProveedor():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'POST':
                pro = models.Proveedor(
                    empresa=request.form.get("txtEmpresa"),
                    direccion=request.form.get("txtDirección"),
                    email=request.form.get("txtEmail"),
                    representante=request.form.get("txtRepresentante"),
                    telefono=request.form.get("txtTelefono"))
                dbSQL.session.add(pro)
                dbSQL.session.commit()
                flash('Proveedor registrado')
            return redirect(url_for('empleado.proveedores'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route("/modificarProveedor", methods=['POST', 'GET'])
@roles_required('empleado')
def modificarProveedor():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'GET':
                id = request.args.get("idProveedor1")
                pro = dbSQL.session.query(models.Proveedor).filter(
                    models.Proveedor.idProveedor == id).first()
                print("AQUI")
                print(request.args.get("txtEmpresa1"))
                pro.empresa = request.args.get("txtEmpresa1")
                pro.direccion = request.args.get("txtDirección1")
                pro.email = request.args.get("txtEmail1")
                pro.representante = request.args.get("txtTelefono1")
                pro.telefono = request.args.get("txtRepresentante1")
                dbSQL.session.add(pro)
                dbSQL.session.commit()
                flash('Proveedor actualizado')
            return redirect(url_for('empleado.proveedores'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('/activarrProveedor', methods=['GET', 'POST'])
@roles_required('empleado')
def activarrProveedor():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'GET':
                id = request.args.get("idProveedor")
                pro = dbSQL.session.query(models.Proveedor).filter(
                    models.Proveedor.idProveedor == id).first()
            pro.active = 1
            dbSQL.session.add(pro)
            dbSQL.session.commit()
            flash('Proveedor activado')
            return redirect(url_for('empleado.proveedores'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

@empleado.route('/eliminarProveedor', methods=['GET', 'POST'])
@roles_required('empleado')
def eliminarProveedor():
    if current_user.has_role('empleado'):
        empleado = True
        try:
            if request.method == 'GET':
                id = request.args.get("idProveedor")
                pro = dbSQL.session.query(models.Proveedor).filter(
                    models.Proveedor.idProveedor == id).first()
            pro.active = 0
            dbSQL.session.add(pro)
            dbSQL.session.commit()
            flash('Proveedor eliminado')
            return redirect(url_for('empleado.proveedores'))
        except:
            flash('Ha ocurrido un error al consultar la información')
            return render_template('error.html')
    flash('No tienes permiso para acceder a este apartado')
    return redirect(url_for('main.index'))

# ------------------------------ FIN PROVEEDOR CRUD ----------------------------------