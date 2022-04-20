import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_database')

try:
    with conexion:
        with conexion.cursor() as cursor:
            sentencia = 'SELECT * FROM "PERSONA" WHERE id_persona = %s'
            id_persona = input('Proporciona el valor id_pesona: ')

            # Para el metodo execute pasamos los parametros de sentencia y la tupla de valores proporiconados por el usuario
            cursor.execute(sentencia, (id_persona,))

            registros = cursor.fetchone()
            print(registros)

except Exception as e:
    print(f'Ocurrió un error: {e}')
finally:
    conexion.close()