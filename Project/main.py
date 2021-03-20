
# import datetime module
import datetime
# import pymongo module
import pymongo
import dns
# connection string
from flask import Blueprint, render_template, request,session, Flask
from flask.helpers import url_for
from flask_security import login_required, current_user
from flask_security.decorators import roles_required
from flask_sqlalchemy import model
from werkzeug.utils import redirect
from . import db
from . import models
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


client = pymongo.MongoClient(
    "mongodb+srv://admin:gmJR1NOhBmEEQm9t@cluster0.c8eub.mongodb.net/myFirstDatabase?retryWrites=true&w=majority")
# test
try:
    db = client['ayuda_humanitaria']
    # define collection
    collection = db['sede']
    if db:
        print('✅ Coneccion establecida '+ str(collection))

except Exception as e:
    print('❌ Coneccion no establecida')
    print(e)
'''
# sample data
document = {"ciudad":"Capital One",
"direccion":"McLean",
"director":"VA"}
# insert document into collection
id = collection.insert_one(document).inserted_id
print("id")
Hola edgar como estas?
Muy bien y tú?
'''
