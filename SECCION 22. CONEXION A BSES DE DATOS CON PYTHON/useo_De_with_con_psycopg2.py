from typing import final
import psycopg2



# credenciales para la conexion a las base de datos

conexion = psycopg2.connect(
        user = "postgres",
        password = "admin",
        host = "localhost",
        port = "5432",
        database = "test_db"
)

try:
    with conexion:

        # La diferencia de mandar a llamar el cursor con with, es que automaticamente se cerrara ek cursor
        with conexion.cursor() as cursor:
            cursor.execute("SELECT * FROM persona")
            datos = cursor.fetchall()
            print(datos)

finally:
    conexion.close()