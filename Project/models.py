from collections import defaultdict
from . import dbSQL
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import shortuuid
from datetime import datetime

hoy = datetime.now()

# Definiendo la tabla relacional
users_roles = dbSQL.Table('users_roles',
                          dbSQL.Column('userId', dbSQL.Integer,
                                       dbSQL.ForeignKey('user.id')),
                          dbSQL.Column('roleId', dbSQL.Integer, dbSQL.ForeignKey('role.id')))


class User(UserMixin, dbSQL.Model):
    """User account model"""

    __tablename__ = 'user'
    id = dbSQL.Column(dbSQL.Integer, primary_key=True)
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
