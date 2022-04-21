from logging import exception
from typing import final
import psycopg2

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_database')

# try:
#     with conexion:
#         with conexion.cursor() as cursor:
            
#             sentencia = 'DELETE FROM "PERSONA" WHERE "Id_persona"=%s'
#             valor = input("Ingrese el ID del registro a eliminar: ")
            
#             regEliminados = cursor.rowcount
#             cursor.execute(sentencia,valor)
            
#             print("Registros eliminados: ", regEliminados)

# except Exception as e:
#     print(e)

# finally:
#     conexion.close()




# Eliminar varios registros
# ------------------------------------------------------------------------------------------------------------------------------

try:
    with conexion:
        with conexion.cursor() as cursor:
            
            sentencia = 'DELETE FROM "PERSONA" WHERE "Id_persona" IN %s'
            entrada = input("Ingrese el ID del registro a eliminar: ")
            
            # split lo que hace es recoppilar mas de una valor que se ingrese y separalos por ","
            valores = (tuple(entrada.split(',')),)
            regEliminados = cursor.rowcount
            cursor.execute(sentencia,valores)
            
            print("Registros eliminados: ", regEliminados)

except Exception as e:
    print(e)

finally:
    conexion.close()
    
    
    


