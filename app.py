import os
from flask import Flask
from flask import url_for
from flask import render_template
from psycopg2 import connect
from modelos.modelo00_bd import cadenaConexion
from flask import session
from flask import redirect
from flask import request
from blueprints.bd01_login import obj_login
from blueprints.bd02_productos import bp_productos
from blueprints.bd03_pagar import bp_pagar
from blueprints.bd04_reporte_ventas import bp_ventas
from blueprints.bd05_configuracion import bp_configuracion

#Creacion y asignacion de la app

mi_app = Flask(__name__)

#Creacion de la llave secreta

mi_app.secret_key="practica"

#Creacion de rutas

@mi_app.route('/')

def inicio():
    return render_template('m01_login/p01_login.html')


mi_app.register_blueprint(obj_login)
mi_app.register_blueprint(bp_productos)
mi_app.register_blueprint(bp_pagar)
mi_app.register_blueprint(bp_ventas)
mi_app.register_blueprint(bp_configuracion)



if __name__ == '__main__': 
    mi_app.run(host="127.0.0.1", port = 5000, debug=True) 