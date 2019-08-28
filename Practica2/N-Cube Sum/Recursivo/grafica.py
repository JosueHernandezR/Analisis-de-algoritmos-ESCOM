# Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Suma de las primeras n cúbicas "Recursivo"
# Este archivo hará que el programa principal grafica los datos obtenidos con el algoritmo

import matplotlib.pyplot as plt
import numpy as np

def grafica ( _c, parameters, n ):
    t, c = [ ], [ ]
    # Título de la ventana.
    plt.figure ( "Primeras 'n' Cúbicas: Algoritmo Recursivo" )
    # Título de la gráfica.
    plt.title ( "CubeSum ( " + str ( n ) + " ): " + str ( _c [ 0 ] ) )
    # Parámetro Tiempo (t) y Cubo (n) de la gráfica.
    c = np.arange ( 0, len ( parameters ) )
    t = list ( map ( lambda x: x [ 1 ], parameters ) )
    # Función propuesta: g( n ) = ( 5/2 )n.
    _t = list ( map ( ( lambda x: x * ( 5 / 2 ) ), t ) )
    # Nombre de los ejes
    plt.ylabel ( "Tiempo ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.xlabel ( "CubeSum ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( c, _t, "b--")
    plt.plot ( c, _t, "b^", label = "g( n ) = ( 5/2 )( n )" )
    plt.plot ( c, t, "ro", label = "T( n ) = ( n )" )
    plt.plot ( c, t, "r--")
    plt.legend ( loc = "lower right" )
    plt.show ( )