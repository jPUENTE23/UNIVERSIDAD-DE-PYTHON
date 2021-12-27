from SERVICIO.catalogoPeliculas import CataloloPeliculas


# Mirar la seccion de contextp estatico


if __name__ == "__main__":
    while True:
        print("[1]. AGREGAR PELICULA")
        print("[2]. LISTAR PELICULAS")
        print("[3]. ELIMINAR ARCHICO DE PELICULAS")
        print("[3]. SALIR")
        opcion = int(input("ELIJA UNA DE LAS OPCIONES: "))
        if opcion == 1:
            nombrePelicula = input("Nombre Pelicula: ")
            onjeto = CataloloPeliculas(nombrePelicula)
            onjeto.agregar_pelicula()

        elif opcion == 2:
            CataloloPeliculas.listas_peliculas()

        elif opcion ==3:
            CataloloPeliculas.Eliminar()
            print("EL ARCHIVO SE ELIMINO CORRECTAMENTE")

        elif opcion == 4:
            break