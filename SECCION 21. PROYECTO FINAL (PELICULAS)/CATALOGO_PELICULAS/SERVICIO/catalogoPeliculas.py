
import sys
import os

sys.path.insert(0, 'C:\\Users\\jorge\\001 Biblioteca\\UDEMY\\UNIVERSIDAD DE PYTHON_2\\SECCION 21. PROYECTO FINAL (PELICULAS)')

from CATALOGO_PELICULAS.DOMINIO.pelicula import Pelicula

listaPeliculas = []

class CataloloPeliculas(Pelicula):
    ruta_Archivo = "C:\\Users\jorge\\001 Biblioteca\\UDEMY\\UNIVERSIDAD DE PYTHON_2\\SECCION 21. PROYECTO FINAL (PELICULAS)\\Peliculas.txt"

    def __init__(self,NombrePelicula):
        super().__init__(NombrePelicula)

    def agregar_pelicula(self):
        listaPeliculas.append(super().__str__())
        with open (CataloloPeliculas.ruta_Archivo, 'a') as arvhivo:
            for pelicula in listaPeliculas:
                arvhivo.write(f"{pelicula}\n")

    @staticmethod
    def listas_peliculas():
        with open (CataloloPeliculas.ruta_Archivo, 'r') as arvhivo:
            for pelicula in arvhivo:
                print("\n" + pelicula)

    @staticmethod
    def Eliminar():
        os.remove(CataloloPeliculas.ruta_Archivo)

