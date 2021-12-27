from typing import final
import psycopg2



# credenciales para la conexion a las base de datos

try:
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