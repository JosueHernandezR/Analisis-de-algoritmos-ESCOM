#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Iterativo
from fibonacci import fibonacci
from grafica import graph

def main ( ):
    n = -1
    while ( n <= 0 ):
        n = int ( input ( "\n\tFibonacci Number to Calculate: " ) )
    # fibonacci (n): devuelve el número de fibonacci, el contador que lleva a 
    # encuentrar ese número y una lista de los números de fibonacci antes de 'fibo'.
    fibo, count, f = fibonacci ( n )
    print(count)
    print ( "\n\tFibonacci ( ", n, " ): ", fibo, "\n" )
    graph ( count, fibo, f, n )
main ( )