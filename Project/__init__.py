from flask import Flask, render_template, flash
from flask.helpers import url_for
from sqlalchemy import exc
from flask_sqlalchemy import SQLAlchemy
from flask_security import Security, SQLAlchemyUserDatastore
import os

from werkzeug.utils import redirect
# Creamos una instancia de SQLAlchemy

dbSQL = SQLAlchemy()
from . models import User,Role
userDataStore = SQLAlchemyUserDatastore(dbSQL, User, Role)


def create_app():
    # Creamos una instancia del flask
    
        app = Flask(__name__)

        app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        # Generar la clave de sessión para crear una cookie con la inf. de la sessión
        app.config['SECRET_KEY'] = os.urandom(24)
        
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root12@localhost:3303/tiendaflask'
        app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'
        #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://pizzadev:idgs801!@192.168.0.108:3306/tiendaflask'

        app.config['SECURITY_PASSWORD_SALT'] = 'thissecretsalt'
        dbSQL.init_app(app)

        
        @app.before_first_request
        def create_all():
            try:
                dbSQL.create_all()
            except exc.SQLAlchemyError:
                flash('Error al conectarse al servidor')
                return redirect(url_for('main.error'))

        @app.errorhandler(500)
        def base_error_handler(e):
            return render_template('erorr.html'), 500

        @app.errorhandler(404)
        def page_not_found(e):
            # note that we set the 404 status explicitly
            flash('Recurso no encontrado')
            return render_template('404.html'), 404
        #Vincula los modelos a flask-security
        security = Security(app, userDataStore)

        # Registramos el blueprint para las rutas auth
        from .auth import auth as auth_blueprint
        app.register_blueprint(auth_blueprint)

        # Registramos el blueprint para las rutas admin
        from .admin import admin as admin_blueprint
        app.register_blueprint(admin_blueprint)
        
        #Registramos el blueprint para las rutas empleado
        from .empleado import empleado as empleado_blueprint
        app.register_blueprint(empleado_blueprint)

        # Registramos el blueprint para el resto de la aplicación
        from .main import main as main_blueprint
        app.register_blueprint(main_blueprint)

        return app
    