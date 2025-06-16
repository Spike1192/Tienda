import psycopg2
from datetime import date, datetime
from flask import current_app

from  modelos.modelo00_bd   import   cadenaConexion 
from modelos.modelo04_Generar_Pdf import generar_pdf_venta

def buscar_producto_por_codigo(codigo):
    conexion = cadenaConexion()
    cursor = conexion.cursor()
    cursor.execute("""
        SELECT nomprod, cantprod, precio FROM productos
        WHERE codprod = %s AND fkcods = 1
    """, (codigo,))
    producto = cursor.fetchone()
    conexion.close()
    if producto:
        return {'producto': producto[0], 'stock': producto[1], 'precio': float(producto[2])}
    else:
        return None

def guardar_venta_y_retornar_pdf(cliente, total, productos):
    conn = cadenaConexion()
    cursor = conn.cursor()

    cursor.execute("INSERT INTO venta (cliente, total, fecha, hora) VALUES (%s, %s, CURRENT_DATE, CURRENT_TIME) RETURNING nv", (cliente, total))
    nv = cursor.fetchone()[0]

    for p in productos:
        cursor.execute(
            "INSERT INTO detalleventa (producto, cantidad, precio, fknv) VALUES (%s, %s, %s, %s)",
            (p['producto'], p['cantidad'], p['precio'], nv)
        )
        # Aquí actualizamos el stock del producto restando la cantidad vendida
        cursor.execute(
            "UPDATE productos SET cantprod = cantprod - %s WHERE codprod = %s",
            (p['cantidad'], p['codigo'])
        )

    conn.commit()
    cursor.close()
    conn.close()

    buffer = generar_pdf_venta(nv, cliente, total, productos)
    return buffer, nv

def buscar_productos_por_nombre(nombre):
    
    conn = cadenaConexion()
    cursor = conn.cursor()
    cursor.execute("""
        SELECT codprod, nomprod, cantprod, precio
        FROM productos
        WHERE fkcods = 1 AND nomprod ILIKE %s
        LIMIT 10;
    """, (f"%{nombre}%",))
    filas = cursor.fetchall()
    conn.close()
    return[
        {
            "codigo": r[0],
            "producto": r[1],
            "stock": r[2],
            "precio": float(r[3])  # importante si estás devolviendo JSON
        }
        for r in filas
    ]
