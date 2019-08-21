#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Suma Binaria
# Este es el archivo principal donde se ejecutan las funciones
# hechas en otros archivos para una mejor legibilidad




from SumaBinaria import binarysum
from random import random
from Grafica import graph

# n y m son de orden Dos a la potencia de n (2 ^ (n)) puede ser (n> m) o (n = m) pero nunca (n <m).
# c: Almacena la suma binaria de 'a' y 'b'.
# a: almacena la primera lista binaria.
# b: almacena la segunda lista binaria.
# n: es el tamaño de ambas listas.

def display ( a, b, c, counter ):
    DATAFORMAT = ""
    if ( len ( c ) > len ( a ) ): DATAFORMAT = "   "

    print ( "\n\tA: " + DATAFORMAT, a )
    print ( "\tB: " + DATAFORMAT, b )
    print ( "\tC: ", c )
    print ( "\n\tOrden de la suma: ", int ( pow ( 2, len ( c ) - 1 ) ), "\n" )
    print ( "\tTamaño de lista 'Suma': ", len ( c ), "\t\tTime: ", counter, "\n" )

def generate ( ):
    a, b, n, m = [ ], [ ], 0, 1
    # Defina el tamaño de las listas a-b (n-m respectivamente).
    while ( n < m ):
        rnd = ( int ( random ( ) * 5 ) + 1 )
        n = int ( pow ( 2, rnd ) )
        print("\tTamaño de lista n", n)
        rnd = ( int ( random ( ) * 5 ) + 1 )
        m = int ( pow ( 2, rnd ) )
        print("\tTamaño de lista m", m)
    # Genere ambos números binarios como listas enteras.
    for i in range ( n ):
        a.insert ( 0, ( ( int ( random ( ) * 2 ) + 0 ) ) )
        if ( i >= m ):
            b.insert ( 0, 0 )
        else:
            b.insert ( 0, ( ( int ( random ( ) * 2 ) + 0 ) ) )
    # Return valores.
    return a, b

def main ( ):
    a, b = generate ( )
    c, count = binarysum ( a, b )
    display ( a, b, c, count )
    graph ( len ( c ), count )
main ( )