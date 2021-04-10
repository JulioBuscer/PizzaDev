from . import dbSQL
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin

from datetime import datetime

hoy = datetime.now()

# Definiendo la tabla relacional
users_roles = dbSQL.Table('users_roles',
                          dbSQL.Column('userId', dbSQL.Integer,
                                       dbSQL.ForeignKey('user.id')),
                          dbSQL.Column('roleId', dbSQL.Integer, dbSQL.ForeignKey('role.id')))

personas_direcciones = dbSQL.Table('personas_direcciones',
                        dbSQL.Column('idPersona', dbSQL.Integer,dbSQL.ForeignKey('Persona.idPersona')),
                        dbSQL.Column('idDireccion', dbSQL.Integer, dbSQL.ForeignKey('Direccion.idDireccion')))

venta_recetario = dbSQL.Table('venta_recetario',
                        dbSQL.Column('idVenta', dbSQL.Integer,dbSQL.ForeignKey('Venta.idVenta')),
                        dbSQL.Column('idRecetario', dbSQL.Integer, dbSQL.ForeignKey('Recetario.idRecetario')),
                        dbSQL.Column('cantidad', dbSQL.Float, nullable=False))

recetario_materiaprima = dbSQL.Table('recetario_materiaprima',
                        dbSQL.Column('idRecetario', dbSQL.Integer, dbSQL.ForeignKey('Recetario.idRecetario')),
                        dbSQL.Column('idMateriaPrima', dbSQL.Integer, dbSQL.ForeignKey('MateriaPrima.idMateriaPrima')),
                        dbSQL.Column('cantidad', dbSQL.Float, nullable=False))
                        

class User(UserMixin, dbSQL.Model):
    """User account model"""

    __tablename__ = 'user'
    id= dbSQL.Column(dbSQL.Integer, primary_key=True)
    name = dbSQL.Column(dbSQL.String(100), nullable=False)
    email = dbSQL.Column(dbSQL.String(100), nullable=False, unique=True)
    password = dbSQL.Column(dbSQL.String(255), nullable=False)
    active = dbSQL.Column(dbSQL.Boolean)
    confirmed_at = dbSQL.Column(dbSQL.DateTime, default=hoy)
    roles = dbSQL.relationship('Role',
                               secondary=users_roles,
                               backref=dbSQL.backref('users', lazy='dynamic'))


class Role(RoleMixin, dbSQL.Model):
    """Role model"""

    __tablename__ = 'role'
    id = dbSQL.Column(dbSQL.Integer, primary_key=True)
    name = dbSQL.Column(dbSQL.String(50), nullable=False)
    description = dbSQL.Column(dbSQL.String(255))


class Persona(dbSQL.Model):
    """ Persona model"""

    __tablename__="Persona"
    idPersona = dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre= dbSQL.Column(dbSQL.String(50), nullable=False)
    apellidoP= dbSQL.Column(dbSQL.String(50), nullable=False)
    apellidoM= dbSQL.Column(dbSQL.String(50), nullable=False)
    telefono= dbSQL.Column(dbSQL.String(12), nullable=False)
    fotografia= dbSQL.Column(dbSQL.Text(), nullable=False)
    usuario = dbSQL.relationship('User', backref=dbSQL.backref('userspersona', lazy='dynamic'))
    direccion = dbSQL.relationship('Direccion',
                                secondary=personas_direcciones,
                                backref=dbSQL.backref('direccionpersona', lazy='dynamic'))
    idUsuario= dbSQL.Column('idUsuario', dbSQL.Integer,dbSQL.ForeignKey('user.id'))


class Direccion(dbSQL.Model):
    """ Direccion model"""

    __tablename__="Direccion"
    idDireccion = dbSQL.Column(dbSQL.Integer, primary_key=True)
    calle= dbSQL.Column(dbSQL.String(50), nullable=False)
    colonia= dbSQL.Column(dbSQL.String(50), nullable=False)
    numeroInt= dbSQL.Column(dbSQL.String(8), nullable=False)
    numeroExt= dbSQL.Column(dbSQL.String(8), nullable=False)
    codigoPostal= dbSQL.Column(dbSQL.Integer, nullable=False)
    descripcion= dbSQL.Column(dbSQL.String(50), nullable=False)


class Venta(dbSQL.Model):
    """ Venta model"""

    __tablename__="Venta"
    idVenta = dbSQL.Column(dbSQL.Integer, primary_key=True)
    cantidad= dbSQL.Column(dbSQL.Integer, nullable=False)
    subtotal= dbSQL.Column(dbSQL.Integer, nullable=False)
    fecha = dbSQL.Column(dbSQL.String(40), nullable=False)
    descripcion= dbSQL.Column(dbSQL.String(100), nullable=False)
    direccion = dbSQL.Column(dbSQL.String(200), nullable=False)
    estatus = dbSQL.Column(dbSQL.Boolean, nullable=False, default=1)
    persona = dbSQL.relationship('Persona', backref=dbSQL.backref('personasventa', lazy='dynamic'))
    recetario= dbSQL.relationship('Recetario',
                                secondary=venta_recetario,
                                backref=dbSQL.backref('recetario', lazy='dynamic'))
    idPersona= dbSQL.Column('idPersona', dbSQL.Integer,dbSQL.ForeignKey('Persona.idPersona'))

class Recetario(dbSQL.Model):
    """Recetario model"""

    __tablename__="Recetario"
    idRecetario = dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre= dbSQL.Column(dbSQL.String(50), nullable=False)
    descripcion= dbSQL.Column(dbSQL.String(50), nullable=False)
    costo= dbSQL.Column(dbSQL.String(8), nullable=False)
    foto= dbSQL.Column(dbSQL.Text, nullable=False)
    active = dbSQL.Column(dbSQL.Boolean, nullable=False, default=1)
    materiaprima= dbSQL.relationship('MateriaPrima',
                            secondary=recetario_materiaprima,
                            backref=dbSQL.backref('recetariosmateriaprima', lazy='dynamic'))


class MateriaPrima(dbSQL.Model):
    """MateriaPrima model"""

    __tablename__="MateriaPrima"
    idMateriaPrima = dbSQL.Column(dbSQL.Integer, primary_key=True)
    nombre= dbSQL.Column(dbSQL.String(50), nullable=False)
    descripcion= dbSQL.Column(dbSQL.String(80), nullable=False)
    categoria= dbSQL.Column(dbSQL.String(20), nullable=False)
    precio= dbSQL.Column(dbSQL.String(10), nullable=False)
    cantidad= dbSQL.Column(dbSQL.Integer, nullable=False)
    fecha= dbSQL.Column(dbSQL.String(40), nullable=False)
    unidad= dbSQL.Column(dbSQL.String(3), nullable=False)
    active = dbSQL.Column(dbSQL.Boolean, nullable=False, default=1)
    idProveedor= dbSQL.Column('idProveedor', dbSQL.Integer,dbSQL.ForeignKey('Proveedor.idProveedor'))
    proveedor = dbSQL.relationship('Proveedor', backref=dbSQL.backref('proveedores', lazy='dynamic'))

class Proveedor(dbSQL.Model):
    """Proveedor model"""

    __tablename__="Proveedor"
    idProveedor = dbSQL.Column(dbSQL.Integer, primary_key=True)
    empresa= dbSQL.Column(dbSQL.String(80), nullable=False)
    direccion= dbSQL.Column(dbSQL.String(80), nullable=False)
    email= dbSQL.Column(dbSQL.String(80), nullable=False)
    representante= dbSQL.Column(dbSQL.String(80), nullable=False)
    telefono= dbSQL.Column(dbSQL.String(80), nullable=False)
    active = dbSQL.Column(dbSQL.Boolean, nullable=False, default=1)