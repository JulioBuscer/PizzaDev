from flask_principal import Permission, RoleNeed
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required
import os
from flask import Flask
<<<<<<< HEAD
<<<<<<< HEAD
from flask_security import Security, SQLAlchemyUserDatastore
from flask_sqlalchemy import SQLAlchemy

#Creamos una instancia de SQLAlchemy
db = SQLAlchemy()
from .models import User, Role
userDataStore = SQLAlchemyUserDatastore(db, User, Role)
=======
=======
>>>>>>> origin/Version
from flask_mongoengine import MongoEngine
# Creamos una instancia de SQLAlchemy
db = MongoEngine()
from .models import User, Role
userDataStore = MongoEngineUserDatastore(db, User, Role)
<<<<<<< HEAD
>>>>>>> origin/main
=======

>>>>>>> origin/Version

def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)
<<<<<<< HEAD
    
<<<<<<< HEAD
        
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        #Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)
    
    app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost/flasksecurity'
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    
    db.init_app(app)
    
    @app.before_first_request
=======
        #Generar la clave de sessión para crear una cookie con la inf. de la sessión
=======

    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
>>>>>>> origin/Version
    app.config['SECRET_KEY'] = os.urandom(24)

    # app.config["MONGODB_HOST"] = "mongodb://localhost:27017/flask_security"
    app.config["MONGODB_HOST"] = "mongodb+srv://admin:gmJR1NOhBmEEQm9t@cluster0.c8eub.mongodb.net/flask_security?authSource=admin&replicaSet=atlas-b00mj0-shard-0&readPreference=primary&appname=MongoDB%20Compass&ssl=true"
    app.config["MONGODB_DB"] = True
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    admin_permission = Permission(RoleNeed('admin'))
    db.init_app(app)

    @app.before_first_request
    def create_user():
        # consultar un registro con filtro
        #pipeline = [{"$match":{"email":"a@example.com"}} ,{"$project": {"_id": 1, "email": 1}}]
        #pipeline = [{"$match":{"email":"a@example.com"}}]
        #user = User.objects().aggregate(pipeline)
        # print(user._CommandCursor__data[0]['_id'])

        # Consultar todos los registros de un documento
        user = User.objects()
        print(user[0]['email'])
        roles = Role.objects
        print(roles[1]['name'])

        test_role = user_datastore.find_or_create_role('test')
       # user_datastore.create_user(
       #     email='a@example.com', password='abc123', roles=[test_role]
       # )
        admin_role = user_datastore.find_or_create_role('admin')
<<<<<<< HEAD
        user_datastore.create_user(
            email='b@example.com', password='abcd1234',
            roles=[admin_role]
        )

    @app.before_first_request
>>>>>>> origin/main
    def create_all():
        try:
            db.create_all()
        except:
            print('error')

    #Vincula los modelos a flask-security
<<<<<<< HEAD
    security = Security(app, userDataStore)

=======
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
>>>>>>> origin/main
    #Configurando el login_manager
    #login_manager = LoginManager()
    #login_manager.login_view = 'auth.login'
    #login_manager.init_app(app)

    #Importamos la clase User.
    #from .models import User
    #@login_manager.user_loader
    #def load_user(user_id):
        #return User.query.get(int(user_id))

    #Registramos el blueprint para las rutas auth
=======
       # user_datastore.create_user(
       #     email='b@example.com', password='abcd1234',
       #     roles=[admin_role]
       # )

    # Vincula los modelos a flask-security
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    # Registramos el blueprint para las rutas auth
>>>>>>> origin/Version
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Registramos el blueprint para el resto de la aplicación
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
