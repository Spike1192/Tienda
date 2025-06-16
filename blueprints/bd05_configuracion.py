from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from modelos.modelo01_login import get_usuario, actualizar_clave


bp_configuracion = Blueprint ('configuracion',__name__)

@bp_configuracion.route('/configuracion')
def configuracion():
    return render_template('m02_gestion/configuracion.html')

@bp_configuracion.route('/actualizar_clave', methods=['POST'])
def actualizar_clave_route():
    data = request.json
    usuario = data.get('usuario').upper()
    clave_actual = data.get('clave_actual')
    clave_nueva = data.get('clave_nueva')

    # Validar si usuario y clave actual son correctos
    usuario_encontrado = get_usuario(usuario, clave_actual)
    if not usuario_encontrado:
        return jsonify({"success": False, "message": "Usuario o contraseña actual incorrectos"}), 400

    # Actualizar la clave
    exito = actualizar_clave(usuario, clave_nueva)
    if exito:
        return jsonify({"success": True, "message": "Contraseña actualizada exitosamente"})
    else:
        return jsonify({"success": False, "message": "Error al actualizar la contraseña"}), 500