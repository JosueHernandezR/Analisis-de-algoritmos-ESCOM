  
import matplotlib.pyplot as plt
import numpy as np

def grafica ( _c, parameters, n ):
    t, c = [ ], [ ]
    # Título de la ventana.
    plt.figure ( "First 'n' Cubes: Recursive Algorithm" )
    # Título de la gráfica.
    plt.title ( "CubeSum ( " + str ( n ) + " ): " + str ( _c [ 0 ] ) )
    # Parámetro Tiempo (t) y Cubo (n) de la gráfica.
    c = np.arange ( 0, len ( parameters ) )
    t = list ( map ( lambda x: x [ 1 ], parameters ) )
    # Función propuesta: g( n ) = ( 5/2 )n.
    _t = list ( map ( ( lambda x: x * ( 5 / 2 ) ), t ) )
    # Nombre de los ejes
    plt.ylabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.xlabel ( "CubeSum ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( c, _t, "b--")
    plt.plot ( c, _t, "b^", label = "g( n ) = ( 5/2 )( n )" )
    plt.plot ( c, t, "ro", label = "T( n ) = ( n )" )
    plt.plot ( c, t, "r--")
    plt.legend ( loc = "lower right" )
    plt.show ( )