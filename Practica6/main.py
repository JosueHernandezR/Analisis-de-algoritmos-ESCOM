#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 6 Divide y vencerás

from maximo_subarreglo import *
import variablesglobales as gb
import random as rnd
from plot import *

__FORMAT_1 = "\n\n\tMaximo subarreglo: algoritmo de fuerza bruta"
__FORMAT_2 = "\n\n\tMaximo subarreglo: algoritmo de cruce"
__FORMAT_3 = "\n\n\tMaximo subarreglo: algoritmo de recurrencia"

def printer ( A, max_left, max_right, result, flag ):
    if ( flag == 1 ):
        print ( "\n\tArreglo a evaluar: {}".format ( A ) )
        print ( __FORMAT_1 )
    elif ( flag == 2 ):
        print ( __FORMAT_2 )
    else:
        print ( __FORMAT_3 )
    print ( "\n\tMáximo Subarreglo: {}".format ( A [ max_left : max_right + 1 ] ) )
    print ( "\n\tSuma: {}\n\n".format ( result ) )

def create ( ):
    n = 2 ** 8
    A = [ rnd.randint ( -n, n ) for i in range ( n ) ]
    return A

if ( __name__ == "__main__" ):
    A = create ( )
    # Encuentra el máximo subarreglo usando el Algoritmo de fuerza bruta.
    for i in range ( len ( A ) + 1 ):
        max_left, max_right, result = fuerza_bruta ( A [ :i ] )
        gb.parametros_1.append ( ( len ( A [ :i ] ), gb.tiempo ) )
        gb.tiempo = 0
    printer ( A, max_left, max_right, result, 1 )
    # Encuentra el máximo subarreglo usando el Algoritmo de cruce.
    for i in range ( len ( A ) + 1 ):
        high = int ( len ( A [ :i ] ) )
        mid = int ( high / 2 )
        max_left, max_right, result = crossing ( A [ :i ], 0, mid, high )
        gb.parametros_2.append ( ( len ( A [ :i ] ), gb.tiempo ) )
        gb.tiempo = 0
    printer ( A, max_left, max_right, result, 2 )
    # Encuentra el máximo subarreglo usando el Algoritmo de recurrecnia.
    for i in range ( 1, len ( A ) + 1 ):
        high = int ( len ( A [ :i ] ) )
        max_left, max_right, result = recurrencia ( A [ :i ], 0, high )
        gb.parametros_3.append ( ( len ( A [ :i ] ), gb.tiempo ) )
        gb.tiempo = 0
    printer ( A, max_left, max_right, result, 3 )
    plot ( )
