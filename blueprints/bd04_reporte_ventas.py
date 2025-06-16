from flask import Blueprint, render_template, request, redirect, url_for, jsonify

from modelos.modelo05_reporte_ventas import obtener_ventas,obtener_ventas_por_fecha, obtener_venta_detalle
from modelos.modelo04_Generar_Pdf import generar_detalle_venta_pdf, generar_ventas_por_fecha
from modelos.modelo05_reporte_ventas import obtener_ventas_por_rango
from modelos.modelo06_reporte_producto import reporte_productos

bp_ventas = Blueprint ('reportes',__name__)

@bp_ventas.route('/reportes/ventas')
def ventas():
    fecha_desde = request.args.get('desde')
    fecha_hasta = request.args.get('hasta')

    if fecha_desde and fecha_hasta:
        ventas = obtener_ventas_por_fecha(fecha_desde, fecha_hasta)
    else:
        ventas = obtener_ventas()

    return render_template('m02_gestion/reporte_ventas.html', ventas=ventas)

@bp_ventas.route('/reportes/ventas/pdf/<int:nv>')
def generar_pdf_venta(nv):
    venta, detalles = obtener_venta_detalle(nv)
    return generar_detalle_venta_pdf(venta, detalles)

@bp_ventas.route('/reportes/ventas/pdf_mensual')
def generar_reporte_mensual():
    fecha_desde = request.args.get("desde")
    fecha_hasta = request.args.get("hasta")

    if not fecha_desde or not fecha_hasta:
        return "Fechas no válidas", 400

    ventas = obtener_ventas_por_rango(fecha_desde, fecha_hasta)

    return generar_ventas_por_fecha(ventas,fecha_desde,fecha_hasta)

@bp_ventas.route('/reportes/productos')
def productos():
    codigo = request.args.get('codigo', None)
    nombre = request.args.get('producto', None)
    filtro = request.args.get('filtro', default=None)

    if request.args.get('mas_vendidos'):
        filtro = 'mas_vendidos'
    elif request.args.get('no_vendidos'):
        filtro = 'no_vendidos'
    elif request.args.get('por_cantidad'):
        filtro = request.args.get('por_cantidad') == 'asc' and 'por_cantidad_asc' or 'por_cantidad_desc'

    productos = reporte_productos(codigo, nombre, filtro)
    return render_template('m02_gestion/reporte_productos.html', productos=productos)

