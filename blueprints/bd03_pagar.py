from flask import Blueprint, render_template, request, redirect, url_for, jsonify, send_file
from modelos.modelo03_pagar import buscar_producto_por_codigo, guardar_venta_y_retornar_pdf
from modelos.modelo03_pagar import buscar_productos_por_nombre
bp_pagar = Blueprint('pagar', __name__)

@bp_pagar.route('/pagar')
def pagar():
    return render_template('m02_gestion/pagar.html')

@bp_pagar.route('/producto/<codigo>')
def obtener_producto(codigo):
    producto = buscar_producto_por_codigo(codigo)
    return jsonify(producto) if producto else ('', 404)

@bp_pagar.route('/registrar_venta', methods=['POST'])
def registrar_venta():
    data = request.get_json()
    cliente = data['cliente']
    total = data['total']
    productos = data['productos']

    pdf_buffer, nv = guardar_venta_y_retornar_pdf(cliente, total, productos)

    return send_file(
        pdf_buffer,
        mimetype='application/pdf',
        as_attachment=False,
        download_name=f"venta_{nv}.pdf"
    )


@bp_pagar.route('/buscar_productos')
def buscar_productos():
    nombre = request.args.get('nombre', '')
    productos = buscar_productos_por_nombre(nombre)
    return jsonify(productos)
