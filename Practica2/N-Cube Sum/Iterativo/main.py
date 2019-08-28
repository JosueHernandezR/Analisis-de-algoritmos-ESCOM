#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Suma de las primeras n cúbicas "Iterativo"
# Este es el programa que ejecutará el algoritmo y los graficara en relación al tiempo.
from grafica import grafica
from cubo import cubo

def main ( ):
    n = int ( input ( "\n\tNumber to calculate firts n-Cubes: " ) )
    # Cubo (n): Devuelve la _suma de los primeros 'n' cubos, el tiempo de cálculo 
    # del algoritmo y una lista de la suma de los enésimos cubos.
    _sum, count, cubelist = cubo ( n )
    print ( "\n\tThe sum of the first ", n, " cubes is: C ( ", n, " ) = ", _sum, "\n" )
    grafica ( _sum, count, cubelist, n )
main ( )