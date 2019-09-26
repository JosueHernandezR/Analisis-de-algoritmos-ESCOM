#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 5 Divide y vencerás


import matplotlib.pyplot as plt
import global_variables as gb
import numpy as np
import math

switcher = {
    1: "Heap-Sort",
    2: "Cocktail-Sort",
    3: "Shell-Sort"
} # Fin del diccionario.

function = ""

def initialize ( ):
    # Parámetros S (n) -tamaño-.
    s_1 = list ( map ( lambda x:x [ 0 ], gb.parameters_1 ) )
    s_2 = list ( map ( lambda x:x [ 0 ], gb.parameters_2 ) )
    s_3 = list ( map ( lambda x:x [ 0 ], gb.parameters_3 ) )
    # Parámetros T (t) -tiempo-.
    t_1 = list ( map ( lambda x:x [ 1 ], gb.parameters_1 ) )
    t_2 = list ( map ( lambda x:x [ 1 ], gb.parameters_2 ) )
    t_3 = list ( map ( lambda x:x [ 1 ], gb.parameters_3 ) )
    # Funciones propuestas.
    p_1 = list ( map ( lambda x: ( 10/8 ) * x, t_1 ) )
    p_2 = list ( map ( lambda x: ( 10/8 ) * x, t_2 ) )
    p_3 = list ( map ( lambda x: ( 10/8 ) * x, t_3 ) )
    # Declaración de devolución.
    return s_1, s_2, s_3, t_1, t_2, t_3, p_1, p_2, p_3

def plot ( algorithm ):
    # Inicializar los puntos de la trama.
    s_1, s_2, s_3, t_1, t_2, t_3, p_1, p_2, p_3 = initialize ( )
    # Título de la ventana.
    plt.figure ( "Maximum Subarray Problem", figsize = ( 14, 7 ) )

    # MÁXIMA FUERZA BRUTA DEL ALGORITMO DEL SUBARREGLO PARA LA GRAFICA

    plt.subplot ( 1, 3, 1 )
    # Figure title.
    plt.title ( "Mejor caso: {} ( {}, {} )".format ( switcher [ algorithm ], gb.parameters_1 [ -1 ] [ 0 ], gb.parameters_1 [ -1 ] [ 1 ] ), size = "small" )
    plt.ylabel ( "Time ( t )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.plot ( s_1, p_1, "#000000", linestyle = "--", label = "" )
    plt.plot ( s_1, t_1, "#0B3B0B", linewidth = 3, label = "" )

    # MÁXIMO CRUCE DE SUBARREGLO DEL GRÁFICO DEL ALGORITMO

    plt.subplot ( 1, 3, 2 )
    # Figure title.
    plt.title ( "Caso Aleatorio: {} ( {}, {} )".format ( switcher [ algorithm ], gb.parameters_2 [ -1 ] [ 0 ], gb.parameters_2 [ -1 ] [ 1 ] ), size = "small" )
    plt.xlabel ( "Size ( n )", color = ( 0.3, 0.4, 0.6 ), size = "large" )
    plt.plot ( s_2, p_2, "#000000", linestyle = "--", label = "" )
    plt.plot ( s_2, t_2, "#610B0B", linewidth = 3, label = "" )

    # ALGORITMO MÁXIMO DE RECURRENCIA DEL SUBARREGLO DEL GRÁFICO

    plt.subplot ( 1, 3, 3 )
    # Figure title.
    plt.title ( "Peor caso: {} ( {}, {} )".format ( switcher [ algorithm ], gb.parameters_3 [ -1 ] [ 0 ], gb.parameters_3 [ -1 ] [ 1 ] ), size = "small" )
    plt.plot ( s_3, p_3, "#000000", linestyle = "--", label = "" )
    plt.plot ( s_3, t_3, "#4C0B5F", linewidth = 3, label = "" )

    plt.show ( )