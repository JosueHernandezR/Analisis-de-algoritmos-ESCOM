"""
Descripción: Este módulo traza la complejidad temporal de los 3 algoritmos.
"""

import matplotlib.pyplot as plt
import variablesglobales as gb
import numpy as np

def initialize ( ):
    # parametros S ( n ) -size-.
    s_1 = list ( map ( lambda x:x [ 0 ], gb.parametros_1 ) )
    s_2 = list ( map ( lambda x:x [ 0 ], gb.parametros_2 ) )
    s_3 = list ( map ( lambda x:x [ 0 ], gb.parametros_3 ) )
    # parametros T ( t ) -time-.
    t_1 = list ( map ( lambda x:x [ 1 ], gb.parametros_1 ) )
    t_2 = list ( map ( lambda x:x [ 1 ], gb.parametros_2 ) )
    t_3 = list ( map ( lambda x:x [ 1 ], gb.parametros_3 ) )
    # Funciones propuestas
    p_1 = list ( map ( lambda x: ( 10/8 ) * x, t_1 ) )
    p_2 = list ( map ( lambda x: ( 10/8 ) * x, t_2 ) )
    p_3 = list ( map ( lambda x: ( 10/8 ) * x, t_3 ) )
    # Return statement.
    return s_1, s_2, s_3, t_1, t_2, t_3, p_1, p_2, p_3

def plot ( ):
    # Inicializar los puntos del gráfico.
    s_1, s_2, s_3, t_1, t_2, t_3, p_1, p_2, p_3 = initialize ( )
    # Título de la ventana
    plt.figure ( "Problema del máximo subarreglo", figsize = ( 14, 7 ) )

    # MÁXIMA FUERZA BRUTA DEL ALGORITMO DEL SUBARREGLO PARA LA GRAFICA

    plt.subplot ( 1, 3, 1 )
    # Título de la figura
    plt.title ( "Máximo Subarreglo de fuerza bruta ( {}, {} )".format ( gb.parametros_1 [ -1 ] [ 0 ], gb.parametros_1 [ -1 ] [ 1 ] ), size = "small" )
    plt.ylabel ( "Tiempo ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.plot ( s_1, p_1, "#000000", linestyle = "--", label = "3/2 n^2" )
    plt.plot ( s_1, t_1, "#0B3B0B", linewidth = 3, label = "n^2" )
    plt.legend ( loc = "upper left" )

    # MÁXIMO CRUCE DE SUBARREGLO DEL GRÁFICO DEL ALGORITMO

    plt.subplot ( 1, 3, 2 )
    # Título de la figura
    plt.title ( "Máximo cruce de subarreglo ( {}, {} )".format ( gb.parametros_2 [ -1 ] [ 0 ], gb.parametros_2 [ -1 ] [ 1 ] ), size = "small" )
    plt.xlabel ( "Tamaño ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.plot ( s_2, p_2, "#000000", linestyle = "--", label = "3/2 n" )
    plt.plot ( s_2, t_2, "#610B0B", linewidth = 3, label = "n" )
    plt.legend ( loc = "upper left" )

    # ALGORITMO MÁXIMO DE RECURRENCIA DEL SUBARREGLO DEL GRÁFICO

    plt.subplot ( 1, 3, 3 )
    # Título de la figura
    plt.title ( "Máximo Subarreglo ( {}, {} )".format ( gb.parametros_3 [ -1 ] [ 0 ], gb.parametros_3 [ -1 ] [ 1 ] ), size = "small" )
    plt.plot ( s_3, p_3, "#000000", linestyle = "--", label = "3/2 n log ( n )" )
    plt.plot ( s_3, t_3, "#4C0B5F", linewidth = 3, label = "n log ( n )" )
    plt.legend ( loc = "upper left" )

    plt.show ( )