#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Algoritmo de Euclides
# Este archivo contiene las dos formas de resolver la práctica
# La opcion 1 es hacerlo de manera aleatoria
# La opcion 2 es hacerlo mediante la introduccion de numeros de fibonacci


from euclides import algoritmo
from random import random
from grafica import grafica
from fibonacci import *

# r: Almacena el resto de la division de ( n/m ).
# mcd: Almacena el divisor común más grande.
# 'n' and 'm' Son dos números aleatorios.

def menu ( ):
    ans = 0
    print ( "\n\n\t\tAlgoritmo de Euclides:" )
    while ( ans != 1 and ans != 2 ):
        print ( "\n\t1.- Calcular MCD usando números aleatorios." )
        print ( "\t2.- Calcular MCD de números de Fibonacci." )
        ans = int ( input ( "\tResponde [1/2]: " ) )
    # Declaración de devolución.
    return ans

def display ( n, m, mcd ):
    print ( "\n\tMáximo común divisor:MCD ( ", n, ", ", m, " ) = ", mcd, "\n" )

def generate ( ):
    n, m = 0, 1
    while ( n < m ):
        n = ( int ( random ( ) * 1000 ) + 1 )
        print (n)
        m = ( int ( random ( ) * 1000 ) + 1 )
        print (m)
    # Declaración de devolución.
    return n, m

def main ( ):
    ans = menu ( )
    if ( ans == 2 ):
        print ( "\n\tPrimera 'n' de Fibonacci para calcular: " )
        limit = int ( input ( "\tAnswer: " ) )
        # Devuelve una lista de números de Fibonacci.
        fibo = fibolist ( limit )
        # Asigna los dos últimos Fibonacci en la lista.
        n, m = fibo [ len ( fibo ) - 1 ], fibo [ len ( fibo ) - 2 ]
    else:
        # Generar números aleatorios.
        n, m = generate ( )
    # Regreso: mcd, contador de algoritmos para complejidad temporal y lista de procesos mcd.
    resultado, count, mcd = algoritmo ( n, m )
    # Muestra el resultadoado
    display ( n, m, resultado )
    # Gráfico de la Complejidad Temporal del Algoritmo Euclidiano.
    grafica ( n, m, count, mcd )

main ( )