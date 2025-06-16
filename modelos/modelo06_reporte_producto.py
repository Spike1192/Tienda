from psycopg2 import connect
from psycopg2.extras import RealDictCursor

from  modelos.modelo00_bd   import   cadenaConexion 

def reporte_productos(codigo=None, nombre=None, filtro=None):
    conn = cadenaConexion()
    cur = conn.cursor()

    base = """
    SELECT 
        p.codprod,
        p.nomprod,
        p.precio,
        p.cantprod AS stock,
        COALESCE(SUM(dv.cantidad), 0) AS cantidad_vendida,
        p.fkcods
    FROM productos p
    LEFT JOIN detalleventa dv ON p.nomprod = dv.producto
    WHERE 1=1
    """
    params = []

    # Filtros básicos
    if codigo:
        base += " AND p.codprod::text = %s"
        params.append(codigo)
    if nombre:
        base += " AND p.nomprod ILIKE %s"
        params.append(f"%{nombre}%")
    if filtro == "no_vendidos":
        base += " AND p.fkcods = 0"

    base += " GROUP BY p.codprod, p.nomprod, p.precio, p.cantprod, p.fkcods"

    # Orden según filtro
    if filtro == "mas_vendidos":
        base += " ORDER BY cantidad_vendida DESC"
    elif filtro == "stock_mayor":
        base += " ORDER BY p.cantprod DESC"
    elif filtro == "stock_menor":
        base += " ORDER BY p.cantprod ASC"
    else:
        base += " ORDER BY p.codprod"

    cur.execute(base, params)
    productos = cur.fetchall()
    cur.close()
    conn.close()

    return productos