from psycopg2 import connect

def cadenaConexion():
    
    conexion = connect(host="localhost",
                       port = 5432,
                       dbname = "gestionventasinventario",
                       user = "postgres",
                       password = "123456")
    return conexion