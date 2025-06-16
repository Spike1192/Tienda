from flask import Blueprint, render_template, request, redirect, url_for, jsonify
from modelos.modelo02_productos import (
    obtener_productos,
    agregar_producto,
    modificar_producto,
    eliminar_producto,
    obtener_producto_por_codigo
)

bp_productos = Blueprint('productos', __name__)

@bp_productos.route('/productos')
def productos():
    lista = obtener_productos()
    return render_template('m02_gestion/productos.html', productos=lista)

@bp_productos.route('/productos/agregar', methods=['POST'])
def producto_agregar():
    data = request.json
    agregar_producto(data['codigo'], data['producto'], data['cantidad'], data['precio'])
    return jsonify({"mensaje": "Producto agregado"}), 200

@bp_productos.route('/productos/modificar/<codigo>', methods=['GET'])
def producto_modificar(codigo):
    producto = obtener_producto_por_codigo(codigo)
    if producto:
        return jsonify(producto)
    return jsonify({"mensaje": "Producto no encontrado"}), 404

@bp_productos.route('/productos/actualizar', methods=['POST'])
def producto_actualizar():
    data = request.json
    modificar_producto(data['codigo'], data['producto'], data['cantidad'], data['precio'])
    return jsonify({"mensaje": "Producto actualizado"}), 200

@bp_productos.route('/productos/eliminar/<codigo>', methods=['POST'])
def producto_eliminar(codigo):
    eliminar_producto(codigo)
    return jsonify({"mensaje": "Producto eliminado (status=0)"}), 200
