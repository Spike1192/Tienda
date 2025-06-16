from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from  modelos.modelo00_bd   import   cadenaConexion 

def obtener_productos():
    conn = cadenaConexion()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM productos WHERE fkcods = 1 ORDER BY codprod")
    productos = cur.fetchall()
    conn.close()
    return productos

def agregar_producto(codigo, nombre, cantidad, precio):
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute("""
        INSERT INTO productos (codprod, nomprod, cantprod, precio)
        VALUES (%s, %s, %s, %s)
    """, (codigo, nombre, cantidad, precio))
    conn.commit()
    conn.close()

def obtener_producto_por_codigo(codigo):
    conn = cadenaConexion()
    cur = conn.cursor(cursor_factory=RealDictCursor)
    cur.execute("SELECT * FROM productos WHERE codprod = %s", (codigo,))
    producto = cur.fetchone()
    conn.close()
    return producto

def modificar_producto(codigo, nombre, cantidad, precio):
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute("""
        UPDATE productos
        SET nomprod = %s, cantprod = %s, precio = %s
        WHERE codprod = %s
    """, (nombre, cantidad, precio, codigo))
    conn.commit()
    conn.close()

def eliminar_producto(codigo):
    conn = cadenaConexion()
    cur = conn.cursor()
    cur.execute("""
        UPDATE productos
        SET fkcods = 0
        WHERE codprod = %s
    """, (codigo,))
    conn.commit()
    conn.close()
