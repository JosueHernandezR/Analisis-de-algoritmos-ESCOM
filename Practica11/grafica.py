import matplotlib.pyplot as plt
import numpy as np
import global_variables as gb

def plot ( ):
    # Título de la ventana.
    plt.figure ( "Ciclo Hamiltoniano:" )
    # Parámetro Tiempo (t) y Cubo (n) del gráfico.
    s = list ( map ( lambda x: x [ 0 ], gb.parametros ) )
    t = list ( map ( lambda x: x [ 1 ], gb.parametros ) )
    # Función propuesta: g (n) = (5/3) n.
    _t = [ 5/3 * i ** 2 for i in range ( t [ 0 ], len ( gb.parametros ) + t [ 0 ] ) ]
    # Names of the axes.
    plt.ylabel ( "Tiempo ( t )", color = ( 0.3, 0.4, 0.6 ))
    plt.xlabel ( "Tamaño del grafo ( n )", color = ( 0.3, 0.4, 0.6 ))
    # Plot.
    plt.plot ( s, _t, "#800000", linestyle = "--", label = "g( n ) = ( 5/3 )( n^2 )" )
    plt.plot ( s, t, "#778899", linewidth = 3, label = "T( n ) = ( n^2 )" )
    plt.legend ( loc = "lower right" )
    plt.show ( )