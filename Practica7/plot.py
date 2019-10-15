import matplotlib.pyplot as plt
import variables_globales as gb
import numpy as np
import math

function = "Función del algoritmo de Strassen: f ( n ) = n^2.81"
_function = ""

def plot ( ):
    global function, _function
    # Título de la ventana.
    plt.figure ( "Algoritmo de Strassen", figsize = ( 14, 7 ) )
    # Título del gráfico.
    plt.title ( "Strassen ( " + str ( gb.parametros [ -1 ] [ 0 ] ) + ", " + str ( gb.parametros [ -1 ] [ 1 ] ) + " ):", color = ( 0.3, 0.4, 0.6 ), weight = "bold" )
    # Parámetros S (n) -tamaño- del gráfico.
    s = list ( map ( lambda x: x [ 0 ], gb.parametros ) )
    # Parámetros T (t) -tiempo- del gráfico para Strassen.
    t = list ( map ( lambda x: x [ 1 ], gb.parametros ) )
    if ( gb.flag == True ):
        # Compara las complejidades de Strassen con los algoritmos ijk.
        # Parámetros T (t) -tiempo- del gráfico para ijk.
        _t = list ( map ( lambda x: x [ 1 ], gb._parametros ) )
        _function = "Función de algoritmo ijk: g ( n ) = n^3"
    else:
        # En otro caso, proponemos una función asintótica g (n) = 3/2 n ^ 2.81
        # Parámetros T (t) -tiempo- del gráfico.
        _t = list ( map ( lambda x: ( 3/2 ) * x [ 1 ], gb.parametros ) )
        _function = "Función asintótica propuesta: g ( n ) = 3/2 ( n^2.81 )"
    # Nombres de ejes.
    plt.xlabel ( "Size ( n )", color = ( 0.3, 0.4, 0.6 ) )
    plt.ylabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ) )
    # Plot.
    plt.plot ( s, t, "#778899", linewidth = 3, label = function )
    plt.plot ( s, _t, "#800000", linestyle = "--", label = _function )
    plt.legend ( loc = "upper left" )
    plt.show ( )