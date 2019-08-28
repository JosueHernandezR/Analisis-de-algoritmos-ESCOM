
import matplotlib.pyplot as plt
import numpy as np

def grafica ( _sum, count, cubelist, n ):
    # Título de la ventana
    plt.figure ( "First 'n' Cubes: Iterative Algorithm" )
    # Título de la gráfica
    plt.title ( "CubeSum ( " + str ( n ) + " ): " + str ( _sum ) )
    # Parámetro Tiempo (t) y Cubo (n) de la gráfica.
    t = np.arange ( 0, count, ( count / ( len ( cubelist ) ) ) )
    # Parámetro CubeSum (n) del gráfico.
    c = np.arange ( 0, len ( cubelist ) )
    # Función propuesta: g( n ) = ( 5/2 )n.
    _t = list ( map ( ( lambda x: x * ( 5/ 2 ) ), t ) )
    # Nombre de los ejes.
    plt.ylabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.xlabel ( "CubeSum ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( c, _t, "b--")
    plt.plot ( c, _t, "b^", label = "g( n ) = ( 5/2 )( n )" )
    plt.plot ( c, t, "ro", label = "T( n ) = ( n )" )
    plt.plot ( c, t, "r--")
    plt.legend ( loc = "lower right" )
    plt.show ( )