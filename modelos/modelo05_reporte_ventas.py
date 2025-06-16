from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from  modelos.modelo00_bd   import   cadenaConexion 

def obtener_ventas():
    conn = cadenaConexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nv,cliente, total  , fecha, TO_CHAR(hora, 'HH24:MI:SS')
        FROM venta
        WHERE fkcods = 1
        ORDER BY fecha DESC, hora DESC;
    """)
    ventas = cursor.fetchall()
    cursor.close()
    conn.close()
    return ventas

def obtener_ventas_por_fecha(fecha_desde, fecha_hasta):
    conn = cadenaConexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nv, cliente, total, fecha, TO_CHAR(hora, 'HH24:MI:SS')
        FROM venta
        WHERE fkcods = 1
        AND fecha BETWEEN %s AND %s
        ORDER BY fecha DESC, hora DESC;
    """, (fecha_desde, fecha_hasta))
    ventas = cursor.fetchall()
    cursor.close()
    conn.close()
    return ventas

def obtener_venta_detalle(nv):
    conn = cadenaConexion()
    cursor = conn.cursor(cursor_factory=RealDictCursor)

    # Obtener datos de la venta
    cursor.execute("""
        SELECT nv, cliente, total, fecha, TO_CHAR(hora, 'HH24:MI:SS') as hora
        FROM venta
        WHERE nv = %s
    """, (nv,))
    venta = cursor.fetchone()

    # Obtener detalle de la venta
    cursor.execute("""
        SELECT producto, cantidad, precio
        FROM detalleventa
        WHERE fknv = %s
    """, (nv,))
    detalles = cursor.fetchall()

    cursor.close()
    conn.close()
    return venta, detalles

def obtener_ventas_por_rango(fecha_desde, fecha_hasta):
    conn = cadenaConexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT nv, cliente, total, fecha, TO_CHAR(hora, 'HH24:MI:SS')
        FROM venta
        WHERE fkcods = 1 AND fecha BETWEEN %s AND %s
        ORDER BY fecha DESC, hora DESC;
    """, (fecha_desde, fecha_hasta))
    ventas = cursor.fetchall()
    conn.close()
    return ventas

