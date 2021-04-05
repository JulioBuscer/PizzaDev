from flask import Flask
from flask_principal import Permission, RoleNeed
from flask_mongoengine import MongoEngine
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, MongoEngineUserDatastore, SQLAlchemyUserDatastore, UserMixin, RoleMixin, login_required
from werkzeug.security import generate_password_hash, check_password_hash
from pymongo import MongoClient
import os
# Creamos una instancia de SQLAlchemy
dbSQL = SQLAlchemy()
from . models import User, Role
userDataStore = SQLAlchemyUserDatastore(dbSQL, User, Role)
# Creamos una instancia de PyMongo
cluster = MongoClient(
    "mongodb+srv://admin:gmJR1NOhBmEEQm9t@cluster0.c8eub.mongodb.net/pizza_dev?authSource=admin&replicaSet=atlas-b00mj0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true")
dbMongo = cluster['pizza_dev']
print(dbMongo.list_collection_names())
''' Creamos una instancia de MongoEngine
dbMongo = MongoEngine()
from .models import User, Role
userDataStore = MongoEngineUserDatastore(dbSQL, User, Role)
'''


def create_app():
    #Creamos una instancia del flask
    app = Flask(__name__)

    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
    #Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)
<<<<<<< HEAD
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/tiendaflask'
=======
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'
>>>>>>> Edgar
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    dbSQL.init_app(app)

    @app.before_first_request
    def create_all():
        dbSQL.create_all()

    #Vincula los modelos a flask-security
    security = Security(app, userDataStore)

    #Registramos el blueprint para las rutas auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    #Registramos el blueprint para las rutas admin
    from .admin import admin as admin_blueprint
    app.register_blueprint(admin_blueprint)

    #Registramos el blueprint para el resto de la aplicación
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)



    return app


'''
def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)

    # app.config["MONGODB_HOST"] = "mongodb://localhost:27017/flask_security"
    app.config["MONGODB_HOST"] = "mongodb+srv://admin:gmJR1NOhBmEEQm9t@cluster0.c8eub.mongodb.net/flask_security?authSource=admin&replicaSet=atlas-b00mj0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    app.config["MONGODB_DB"] = True
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    admin_permission = Permission(RoleNeed('admin'))
    dbSQL.init_app(app)

    @app.before_first_request
    def create_user():
        # consultar un registro con filtro
        #pipeline = [{"$match":{"email":"a@example.com"}} ,{"$project": {"_id": 1, "email": 1}}]
        #pipeline = [{"$match":{"email":"a@example.com"}}]
        #user = User.objects().aggregate(pipeline)
        # print(user._CommandCursor__data[0]['_id'])

        # Consultar todos los registros de un documento
        #user = User.objects()
        # print(user[0]['email'])
        #roles = Role.objects
        # print(roles[1]['name'])

        # passw = generate_password_hash("1234", method='sha256')
        # test_role = user_datastore.find_or_create_role('test')
        # user_datastore.create_user(
        #     email='a@example.com', password='abc123', roles=[test_role]
        # )
        #admin_role = user_datastore.find_or_create_role('admin')
        # user_datastore.create_user(
        #    email='b@example.com', password=passw,
        #    roles=[admin_role]
        # )

        # Vincula los modelos a flask-security
        user_datastore = MongoEngineUserDatastore(dbSQL, User, Role)
        security = Security(app, user_datastore)
        # Configurando el login_manager
        #login_manager = LoginManager()
        #login_manager.login_view = 'auth.login'
        # login_manager.init_app(app)

        # Importamos la clase User.
        #from .models import User
        # @login_manager.user_loader
        # def load_user(user_id):
        # return User.query.get(int(user_id))

        # Registramos el blueprint para las rutas auth
        # user_datastore.create_user(
        #     email='b@example.com', password='abcd1234',
        #     roles=[admin_role]
        # )

        # Registramos el blueprint para las rutas auth
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # Registramos el blueprint para el resto de la aplicación
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

    return app
'''