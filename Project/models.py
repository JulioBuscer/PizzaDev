from collections import defaultdict
from . import db
from flask_sqlalchemy import SQLAlchemy
from flask_security import UserMixin, RoleMixin
import shortuuid
from datetime import datetime

hoy = datetime.now()
class Role(RoleMixin, db.Document):
    name = db.StringField(max_length=80, unique=True)
    description = db.StringField(max_length=255)


class User(UserMixin, db.Document):
    email = db.StringField(max_length=255)
    password = db.StringField(max_length=255)
    active = db.BooleanField(default=True)
    confirmed_at = db.DateTimeField(default=hoy)
    roles = db.ListField(db.ReferenceField(Role), default=[])


class Struct: 
    def __init__(self, **entries):
        self.__dict__.update(entries)

    @staticmethod
    def is_active():
        return True

    #@staticmethod
    #def get_id(self, **s):
    #    self.id = s._id
    #    return self.id
    