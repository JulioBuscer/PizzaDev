from .models import User, Role
import os
from flask import Flask
from flask_mongoengine import MongoEngine

from flask_security import Security, MongoEngineUserDatastore, \
    UserMixin, RoleMixin, login_required
from flask_principal import Permission, RoleNeed

# Creamos una instancia de SQLAlchemy
db = MongoEngine()
userDataStore = MongoEngineUserDatastore(db, User, Role)


def create_app():
    # Creamos una instancia del flask
    app = Flask(__name__)

    # Generar la clave de sessión para crear una cookie con la inf. de la sessión
    app.config['SECRET_KEY'] = os.urandom(24)

    app.config["MONGODB_HOST"] = "mongodb://localhost:27017/flask_security"
    app.config["MONGODB_DB"] = True
    app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
    admin_permission = Permission(RoleNeed('admin'))
    db.init_app(app)

    @app.before_first_request
    def create_user():
        test_role = user_datastore.find_or_create_role('test')
        user_datastore.create_user(
            email='a@example.com', password='abc123', roles=[test_role]
        )
        admin_role = user_datastore.find_or_create_role('admin')
        user_datastore.create_user(
            email='b@example.com', password='abcd1234',
            roles=[admin_role]
        )

    @app.before_first_request
    def create_all():
        try:
            db.create_all()
        except:
            print('error')

    # Vincula los modelos a flask-security
    user_datastore = MongoEngineUserDatastore(db, User, Role)
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
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    # Registramos el blueprint para el resto de la aplicación
    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app
