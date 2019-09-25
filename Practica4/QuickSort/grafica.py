#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 4 Divide y vencerás

import matplotlib.pyplot as plt
import numpy as np
import gb


"""
                             Variables globales:
    proposed2: Función propuesta para el algoritmo Quicktime. Dependiendo 
            si el usuario elige ordenar el peor de los casos, esta 
            variable tomará el valor de "g (n) = 3/2 n ^ 2". 
            En otro caso "g (n) = n log (n)".
    proposed1: Función propuesta para el algoritmo de Partición. Dependiendo
            si el usuario elige ordenar el peor de los casos, esta 
            variable tomará el valor de "g (n) = 3/2 n". 
            En otro caso "g (n) = n".
    function2: esta función para Quicksort se mostrará solo si el usuario 
            elige ordenar el peor de los casos y tomará el valor 
            de: "T (n) = n ^ 2".
    function1: esta función para Partición se mostrará solo si el usuario 
            elige ordenar el peor de los casos y tomará el valor 
            de: "T (n) = n".
    g2: esta lista almacenará los valores de la función propuesta para Quicksort.
    g1: Esta lista almacenará los valores de la función propuesta para Partición.
"""

proposed2 = ""
proposed1 = ""
function2 = ""
function1 = ""
g2 = [ ]
g1 = [ ]

"""
Función nlogn referencias a parámetros de registro (n ^ n) o puntos de función
para trazar. Esta es la función propuesta en el gráfico, donde T (n) es el
tiempo computacional de nuestro algoritmo y g (n) la función propuesta
tal que T (n) en ϴ (g (n)).
"""

def nlogn ( ):
    global g2, aux
    f = open ( "n log ( n ).txt", "r" )
    aux = f.readlines ( )
    g2 = list ( map ( lambda x: float ( x ) * 5/4, aux [ : len ( gb.n ) + 1 ] ) )
    f.close ( )

"""
Las etiquetas de función están controladas implícitamente por menu.py, dependiendo del valor de
gb.flag (verdadero o falso) asignará valor a las variables globales de cadena y
ayudarán a distinguir el tiempo propuesto y el algoritmo computacional
en el gráfico
"""

def labels ( ):
    global proposed2, proposed1, function2, function1, g1
    g1 = list ( map ( lambda x: 3/2 * x [ 1 ], gb._parameters ) )
    nlogn ( )
    if ( gb.flag ):
        # Worst case labels assignation.
        proposed2 = "g( n ) = ( 3/2 ) n^2"
        proposed1 = "g( n ) = ( 3/2 ) n"
        function2 = "T( n ) = n^2"
        function1 = "T( n ) = n"
    else:
        g1 = list ( np.arange ( 6, max ( g1 ) + 6, max ( g1 ) / len ( gb.n ) ) )
        # Any other case labels assignation.
        proposed2 = "g( n ) = n log ( n )"
        proposed1 = "g( n ) = n"
        function2 = None
        function1 = None

def graph ( ):
    labels ( )
    # Window title.
    plt.figure ( "Algoritmo Quicksort", figsize = ( 14, 7 ) )

    # Right graph: Temporal complexity of Partition.
    plt.subplot ( 1, 2, 2 )
    # Figure title.
    plt.title ( "Partition ( " + str ( gb._parameters [ -1 ] [ 0 ] + 1 ) + ", " + str ( gb._parameters [ -1 ] [ 1 ] ) + " )" )
    # Parameter Time ( t ).
    _t = list ( map ( lambda x: x [ 1 ], gb._parameters ) )
    # Parameter Size ( n ).
    _s = list ( map ( lambda x: x [ 0 ] + 1, gb._parameters ) )
    # Axes names.
    plt.xlabel ( "Tamaño ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.ylabel ( "Tiempo Partition ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( _s, _t, "#778899", linewidth = 3, label = function1 )
    plt.plot ( _s, g1, "#800000", linestyle = "--", label = proposed1 )
    plt.legend ( loc = "upper left" )

    # Left graph: Temporal complexity of Quicksort.
    plt.subplot ( 1, 2, 1 )
    # Figure title.
    plt.title ( "Quicksort ( " + str ( gb.parameters [ -1 ] [ 0 ] ) + ", " + str ( gb.parameters [ -1 ] [ 1 ] ) + " )" )
    # Parameter Time ( t ).
    t = list ( map ( lambda x: x [ 1 ], gb.parameters ) )
    # Parameter Size ( n ).
    s = list ( map ( lambda x: x [ 0 ], gb.parameters ) )
    # Axes names.
    plt.xlabel ( "Size ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.ylabel ( "Quicksort Time ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( s, t, "#778899", linewidth = 3, label = function2 )
    plt.plot ( s, g2, "#800000", linestyle = "--", label = proposed2 )
    plt.legend ( loc = "upper left" )
    plt.show ( )