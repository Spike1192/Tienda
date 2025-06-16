from flask import session
from modelos.modelo00_bd import cadenaConexion

def get_usuario(usuario, clave):
    conexion = cadenaConexion()
    cursor = conexion.cursor()

    sql = "SELECT * FROM login WHERE usuario = %s AND clave = %s;"
    datos = (usuario, clave)

    cursor.execute(sql, datos)
    resultado = cursor.fetchone()
    
    cursor.close()
    conexion.close()

    return resultado
    

def actualizar_clave(usuario, nueva_clave):
    try:
        conexion = cadenaConexion()
        cursor = conexion.cursor()
        sql = "UPDATE login SET clave = %s WHERE usuario = %s;"
        datos = (nueva_clave, usuario)
        cursor.execute(sql, datos)
        conexion.commit()
        cursor.close()
        conexion.close()
        return True
    except Exception as e:
        print("Error al actualizar clave:", e)
        return False