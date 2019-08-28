# Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Suma de las primeras n cúbicas "Recursivo"
# Este es el programa que ejecutará el algoritmo y los graficará en relación al tiempo.
from grafica import grafica
from cubo import cubo

def main ( ):
    parameters = [ ]
    n = int ( input ( "\n\tNumber to calculate firts n-Cubes: " ) )
    # cube (n): Devuelve una lista de tuplas con la suma de los números a la
    # potencia '3' y el tiempo computacional del algoritmo [(C (n), T (n))].
    for i in range ( 1, n + 1 ):
        parameters.append ( cubo ( i, 0 ) )
    print ( "\n\tCubesum ( ", n, " ): ", parameters [ len ( parameters ) - 1 ] [ 0 ], "\n" )
    grafica ( parameters [ len ( parameters ) - 1 ], parameters, n )
main ( )