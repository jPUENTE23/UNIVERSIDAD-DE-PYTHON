
# psycopg2 es el paqueta para conectarnos a postgresql

import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_database')
print(conexion)

# INSERTAR VARIOS DATOS CON TUPLA

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO "PERSONA" ("Nombre", "Apellido", "Email") VALUES (%s,%s,%s)'

            valores = (('Cecilia', 'Martinez', 'ceci@gmail.com'),
                       ('Eduardo', 'Cavazos', 'educa@gmail.com'),
                       ('Karen', 'Guerra', 'guerraK@gmail.com'),
                       ('Antonio', 'Soprano', 'tonyso@gmail.com'))

            cursor.executemany(sentencia,valores)
            print("Datos insertados")

            registros_insertados = cursor.rowcount
            print(f"Registros  insertados: {registros_insertados}")

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()