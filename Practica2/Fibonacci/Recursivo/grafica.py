#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Recursivo
# En este archivo se crean las funciones para el graficado del algoritmo

import matplotlib.pyplot as plt
import numpy as np

def graph ( fibo, parameters, n ):
    t, f = [ ], [ ]
    # Título de la ventana.
    plt.figure ( "Fibonacci Recursive Algorithm" )
    # Título de la gráfica.
    #Imprime la ultima pareja de numeros fibonacci
    #print(fibo)
    plt.title ( "Fibonacci ( " + str ( n ) + " ): " + str ( fibo [ 0 ] ) )
    # Tiempo de parámetro (t) y Fibonacci (n) del gráfico.
    f = np.arange ( 0, len ( parameters ) )
    print(f)
    t = list ( map ( ( lambda x: x [ 1 ] ), parameters ) )
    print(t)
    # Funcion propuesta g ( n ) = ( 5/2 ) ( n ).
    _t = list ( map ( ( lambda x: x * ( 5 / 2 ) ), t ) )
    print(_t)
    # Nombre de los ejes
    plt.ylabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.xlabel ( "Fibonacci ( f )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    # Plot.
    plt.plot ( f, t, "ro", label = "T( n ) = ( Φ^cd ..n )" )
    plt.plot ( f, _t, "b^", label = "g( n ) = ( 5/2 )( Φ^n )" )



    plt.plot ( f, _t, "b--")
    plt.plot ( f, t, "r--")
    plt.legend ( loc = "upper left" )
    plt.show ( )