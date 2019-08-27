#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Iterativo
# Este archivo sirve para gráficar los resultados obtenidos
import matplotlib.pyplot as plt
import numpy as np

def graph ( count, fibo, f, n ):
    # Título de la ventana
    plt.figure ( "Fibonacci Iterative Algorithm" )
    # Título de la grafica
    plt.title ( "Fibonacci ( " + str ( n ) + " ): " + str ( fibo ) )
    # Parámetro del tiempo ( t ) de la gráfica.
    t = np.arange ( 0, count, ( count / ( len ( f ) + 1 ) ) )
    _t = list ( map ( ( lambda x: x * ( 5 / 2 ) ), t ) )
    _f = np.arange ( 0, len ( f ) + 1 )
    # Nombre de los ejes.
    plt.xlabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ), family = "cursive", size = "large" )
    plt.ylabel ( "Fibonacci ( f )", color = ( 0.3, 0.4, 0.6 ), family = "cursive", size = "large" )
    # Plot.
    plt.plot ( _f, t, "#778899", linewidth = 3, label = "T( n ) = ( n )" )
    plt.plot ( _f, _t, "#800000", linestyle = "--", label = "g( n ) = ( 5/2 )( n )" )
    plt.legend ( loc = "lower right" )
    plt.show ( )