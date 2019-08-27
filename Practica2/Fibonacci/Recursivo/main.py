#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Recursivo
# En este archivo ejecuta el programa completo
# va insertando las duplas de los numeros fibonacci para después graficarlas
# mediante el uso de listas (parametros)

from fibonacci import fibonacci
from grafica import graph

def main ( ):
    n, parameters = -1, [ ]
    while ( n <= 0 ):
        n = int ( input ( "\n\tFibonacci Number to Calculate: " ) )
    # fibonacci (n): devuelve una lista de tuplas con los números de Fibonacci
    # y el tiempo computacional del algoritmo [(F (n), T (n))].
    for i in range ( 1, n + 1 ):
        parameters.append ( fibonacci ( i, 0 ) )
        #va imprimiendo cada dupla de numeros fibonacci en la lista en cada iteracion del ciclo
        print("\t",parameters)
    print ( "\n\tFibonacci ( ", n, " ): ", parameters [ len ( parameters ) - 1 ] [ 0 ], "\n" )
    # Imprime los números fibonacci guardados en la lista
    print(len(parameters))
    # Crea la gráfia con los parametros creados.
    graph ( parameters [ len ( parameters ) - 1 ], parameters, n )
main ( )