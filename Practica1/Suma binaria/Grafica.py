#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Suma Binaria
# En este archivo se crean las funciones para el graficado del algoritmo


import matplotlib.pyplot as plt
import numpy as np

def graph ( size, time ):
    # Título de la ventana.
    plt.figure ( "Complejidad temporal del algoritmo de suma binaria" )
    # Título de la gráfica.
    plt.title ( "Suma binaria:", color = ( 0.3, 0.4, 0.6 ), weight = "bold" )
    # Construye los parámetros del gráfico.
    t, n = parametros ( size, time )
    # Definir los límites del gráfico.
    plt.xlim ( 0, size )
    plt.ylim ( 0, time )
    # Función propuesta: g ( n ) = ( 5/3 )n.
    _t = list ( map ( ( lambda x: x * 5/3 ), t ) )
    # Nombres de los ejes.
    plt.xlabel ( "Tamaño ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.ylabel ( "Tiempo ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Gráfico.
    plt.plot ( n, _t, 'bs', label = "g( n ) = ( 5/3 )n" )
    plt.plot ( n, t, 'g^', linewidth = 3, label = "E( n ) = n" )
    plt.plot ( n, _t, 'r--', label = "g( n ) = ( 5/3 )n" )
    plt.plot ( n, t, 'b--', linewidth = 3, label = "E( n ) = n" )
    plt.legend ( loc = "lower right" )
    plt.show ( )

def parametros ( size, time ):
    # tiempo frente a puntos de gráfico.
    t, n = [ ], [ 0 ]
    # div: Variable auxiliar que ayuda a trazar el gráfico.
    div = float ( "{0:.2f}".format ( 1 / round ( time / size ) ) )
    # Tiempo ( t ) parametros.
    for i in range ( time ):
        t.append ( i )
    # Tamaño ( n ) parametros.
    for i in range ( time ):
        if ( i != 0 ):
            n.append ( float ( "{0:.2f}".format ( n [ i - 1 ] + div ) ) )
    # Return de valores.
    return t, n