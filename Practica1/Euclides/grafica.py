#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Algoritmo de Euclides
# En este archivo se crean las funciones para el graficado del algoritmo

import matplotlib.pyplot as plt
import numpy as np

def grafica ( n, m, count, mcd ):
    # Título de la ventana.
    plt.figure ( "Complejidad temporal del algoritmo euclidiano" )
    # Título de la gráfica.
    plt.title ( "Euclideano ( " + str ( n ) + ", " + str ( m ) + " ):", color = ( 0.3, 0.4, 0.6 ), weight = "bold" )
    # Parámetro del tiempo ( t ) del gráfico.
    t = np.arange ( 0, count, ( count / len ( mcd ) ) )
    # Parámetro Euclidiano (n) de la lista
    mcd.reverse ( )
    # Nombres de los ejes.
    plt.xlabel ( "Euclides ( e )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.ylabel ( "Tiempo ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Función propuesta: g (n) = (5/3) log (n).
    _t = list ( map ( ( lambda x: x * ( 5 / 3 ) ), t ) )
    # Plot.
    plt.plot ( mcd, _t, 'bs', label = "g( n ) = ( 5/3 ) log ( n )" )
    plt.plot ( mcd, t, 'g^', label = "E( n ) = log ( n )" )
    plt.legend ( loc = "lower right" )
    plt.show ( )