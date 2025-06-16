from flask import Blueprint, render_template, redirect, url_for, request, session
from modelos.modelo00_bd import cadenaConexion
from modelos.modelo01_login import get_usuario

obj_login = Blueprint('login', __name__)

@obj_login.route('/entrar')
def login_formulario():
    xmensaje = ""
    return render_template('m01_login/p01_login.html', mensaje=xmensaje)

@obj_login.route('/pagar', methods=['POST'])
def login_validar():
    xusuario = request.form['txt_usuario'].upper()
    xclave = request.form['txt_clave']

    resultado = get_usuario(xusuario, xclave)

    if resultado:
        session["xlogin"] = True
        session["xnombre"] = resultado[1]  # nombre
        session["xusuario"] = resultado[2]  # usuario
        session["xstatus"] = resultado[4]   # fkcods

        return render_template('m02_gestion/pagar.html')  # Redirige a pagar.html
    else:
        xmensaje = "¡¡¡Acceso Denegado!!!"
        return render_template('m01_login/p01_login.html', mensaje=xmensaje)

@obj_login.route('/salir')
def login_salir():
    session.clear()
    return redirect('/')
