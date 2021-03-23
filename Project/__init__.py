from flask_principal import Permission, RoleNeed
from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required
import os
from flask import Flask
from flask_mongoengine import MongoEngine
# Creamos una instancia de SQLAlchemy
db = MongoEngine()
from .models import User, Role
userDataStore = MongoEngineUserDatastore(db, User, Role)


def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
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
       # user_datastore.create_user(
       #     email='b@example.com', password='abcd1234',
       #     roles=[admin_role]
       # )

    # Vincula los modelos a flask-security
    user_datastore = MongoEngineUserDatastore(db, User, Role)
    security = Security(app, user_datastore)
    # Registramos el blueprint para las rutas auth
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Registramos el blueprint para el resto de la aplicación
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
