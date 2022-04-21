from logging import exception
from sqlite3 import Cursor
from typing import final
from unittest.mock import sentinel
import psycopg2 

conexion = psycopg2.connect(user='postgres',password='admin',host='127.0.0.1',port='5432',database='test_database')



# try:
    
#     # En este apartado indicamos que miestras "conexion.autocommit = False" no se ejecutara ningun cambio en la bse de datos,
#     # si no hasta que se ejecute el comando commit
#     conexion.autocommit = False
#     cursor = conexion.cursor()
#     senetcia = 'INSERT INTO "PERSONA" ("Nombre", "Apellido", "Email") VALUES (%s,%s,%s)'
#     valores = ('Maria', 'Esparza', 'maria@hotmail.com')
#     cursor.execute(senetcia,valores)
    
#     # La funcion de commit es que que hasta que no se ejecute este comando, no se ejecutaran los cambios en la base de datos
#     '''Por ejemplo: en "cursor.execute(senetcia,valores)" estamos indicando que se ejecute la sentencia indicada junto con los valores
#     proporcionados, pero esos datos no se insertaran ya que se esta esperando un comando de tipo commit, una vez que se ejecute el comando de tipo commit
#     entonces las sentencia anterior se ejecutara eh insertara los datos en el modelo'''

#     senetcia = 'UPDATE "PERSONA" SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "Id_persona"=%s'
#     valores = ('Ian','Cook','ian@zoho.com',8)
#     cursor.execute(senetcia, valores)
    
#     conexion.commit()
#     print("e insertaron los datos correctamente, se hizo commit")
# except Exception as e:
    
#     # rollback, es un comando que se ejcutara si llega a ocurrir un error en la sentencia
#     conexion.rollback()
#     print("Se hizo rollbakc de la trasanccion",e)

# finally:
#     conexion.close()



try:

    with conexion:
        with conexion.cursor() as cursor:
            senetcia = 'INSERT INTO "PERSONA" ("Nombre", "Apellido", "Email") VALUES (%s,%s,%s)'
            valores = ('Saul', 'Goodman', 'saulgo@hotmail.com')
            cursor.execute(senetcia,valores)


            senetcia = 'UPDATE "PERSONA" SET "Nombre"=%s, "Apellido"=%s, "Email"=%s WHERE "Id_persona"=%s'
            valores = ('Oli','Sykes','sykes@zoho.com',9)
            cursor.execute(senetcia, valores)

except Exception as e:
    
    # rollback, es un comando que se ejcutara si llega a ocurrir un error en la sentencia
    print("Ocurrio un error",e)

finally:
    conexion.close()

print("Se modificaron los datos correctamente")
