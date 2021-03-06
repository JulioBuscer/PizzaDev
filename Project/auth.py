from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from flask_security import login_required, current_user
from flask_security.utils import login_user, logout_user
from . models import User
from . models import Persona
from . import dbSQL, userDataStore

auth = Blueprint('auth', __name__, url_prefix='/security')


@auth.route('/login_users')
def login_users():
    return render_template('/security/login_users.html')


@auth.route('/login_users', methods=['POST'])
def login_users_post():
    try:
        
        email = request.form.get('email')
        password = request.form.get('password')
        remember = True if request.form.get('remember') else False

        # Consultamos si existe un usuario ya registrado con el email.
        user = User.query.filter_by(email=email).first()

        # Verificamos si el usuario existe, encriptamos el password y lo comparamos con
        # el de la BD.
        if not user or not check_password_hash(user.password, password):
            # Si el usuario no existe o no coinciden los passwords
            flash('El usuario y/o la contraseña son incorrectos')
            # Error de Autenticación
            return redirect(url_for('auth.login_users'))

        # En este punto el usuario tiene los datos correctos
        try:

            # Creamos una sessión y logueamso al usuario.
            login_user(user, remember=remember)
            if current_user.has_role('cliente') or current_user.has_role('admin') or current_user.has_role('empleado'):
                flash('Bienvenido '+current_user.name)
                return redirect(url_for('main.index'))                
            else:
                logout_user()
                flash('No tienes permiso para acceder al sistema')
                return redirect(url_for('auth.login_users'))
        except:
            flash('Error al iniciar sesión')
            return redirect(url_for('auth.login_users'))
    except:
        flash('El usuario y/o la contraseña son incorrectos')
        return redirect(url_for('auth.login_users'))
    return redirect(url_for('main.index'))


@auth.route('/register_user')
def register_user():
    return render_template('/security/register_user.html')


@auth.route('/register_user', methods=['POST'])
def register_user_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')
    

    # Consultamos si existe un usuario ya registrado con el email.
    user = User.query.filter_by(email=email).first()

    if user:
        # El usuario existe y regresamos a la página de registro.
        flash('El correo '+ email +  ' ya está registrado')
        return redirect(url_for('auth.register_user'))
    try:
        # Creamos un nuevo usuario
        cliente_role = userDataStore.find_or_create_role('cliente')
        userDataStore.create_user(name=name, email=email,
                                  password=generate_password_hash(password, method='sha256'), roles=[cliente_role])
        flash('Te has registrado con éxito')
        # Agregamos el usuario a la bd.
        
        dbSQL.session.commit()
    except:
        flash('Error al registrar usuario')

    return redirect(url_for('auth.login_users'))

@auth.route('/logout')
@login_required
def logout():
    # Cerramos la session
    flash('Tu sesión ha finalizado')
    logout_user()
    return redirect(url_for('main.index'))


