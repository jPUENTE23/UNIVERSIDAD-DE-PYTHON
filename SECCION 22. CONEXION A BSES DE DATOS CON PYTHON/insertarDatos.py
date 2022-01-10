import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_deb')

try:
    with conexion:
        with conexion.cursor() as cursor:

            sentencia = 'INSERT INTO persona (Nombre, Apellidos, Email) VALUES (%s,%s,%s)'

            valores = ('Karina', 'Martinez', 'karin@gmail.com')
            cursor.execute(sentencia,valores)
            print("Datos insertados")
            # registros_insertados = cursor.rowcount()
            # print("Registros  insertados: "+str(registros_insertados))

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()