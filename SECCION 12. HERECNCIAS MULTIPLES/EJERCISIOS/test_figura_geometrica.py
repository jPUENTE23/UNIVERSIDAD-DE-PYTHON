from cuadrado import Cuadrado

cuadrado = Cuadrado(4, "rojo")
print(cuadrado.area())
print(cuadrado._color)

# el orden de busqueda es:
# Cuadrado, FiguraGeometrica(izquierda), Color(derecha), Object(Clase Abuela)
print(Cuadrado.mro())