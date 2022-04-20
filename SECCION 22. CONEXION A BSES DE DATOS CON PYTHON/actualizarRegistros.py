from logging import exception
import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_database')

# ACTUALIZAR UN SOLO REGISTRO
# try:
#     with conexion:
#         with conexion.cursor() as cursor:
            
#             sentecnia = 'UPDATE "PERSONA" SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "Id_persona"=%s'
#             valores = ('Lauren','Eve','lauren@outlook.es',2)
#             cursor.execute(sentecnia, valores)
            
#             # cursor.rowcount nos devolvera la cantidad de registros actualizados o insertados
#             regAct = cursor.rowcount
#             print('Regitros actualizados:',regAct)
            
# except Exception as e:
#     print(e)
    
# finally:
#     conexion.close()


# ACTUALIZAR VARIOS REGISTROS

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            sentecnia = 'UPDATE "PERSONA" SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "Id_persona"=%s'
            valores = (('Lauren','Eve','lauren@outlook.es',4),
                       ('Martin','Doherty','martin@zoho..com',3))
            
            # executemany lo usaremos cuando insertemos o actualizemos mas de un registro
            cursor.executemany(sentecnia, valores)
            
            # cursor.rowcount nos devolvera la cantidad de registros actualizados o insertados
            regAct = cursor.rowcount
            print('Regitros actualizados:',regAct)
            
except Exception as e:
    print(e)
    
finally:
    conexion.close()