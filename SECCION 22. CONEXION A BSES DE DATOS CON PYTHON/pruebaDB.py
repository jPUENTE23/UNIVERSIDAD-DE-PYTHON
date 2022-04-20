from typing import final


# psycopg2 es el modulo con le que nos conectaremos a nuestra base de datos
import psycopg2

try:
    
    # credenciales para la conexion a las base de datos
    conexion = psycopg2.connect(
        user = "postgres",
        password = "admin",
        host = "localhost",
        port = "5432",
        database = "test_db"
    )

    cursor = conexion.cursor()
    cursor.execute("SELECT * FROM persona")
    datos = cursor.fetchall()
    print(datos)

finally:
    cursor.close()
    conexion.close()