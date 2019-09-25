#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 4 Divide y vencerás

import numpy as np
import gb

def menu ( ):
    ans, length = -1, -1
    # Opción de menú 1: el usuario debe seleccionar si crear una lista de números aleatorios o
    # una lista en el peor de los casos para el algoritmo, ordenada en orden decreciente.
    while ( ans != 1 and ans != 2 ):
        print ( "\n\n\t\t\tQUICK-SORT\n\n\t Selecciona una de las siguientes opciones." )
        print ( "\n\t1.- Caso aleatorio." )
        print ( "\t2.- Peor caso." )
        ans = int ( input ( "\Respuesta: " ) )
    # Opción de menú 2: el usuario debe elegir la longitud de la lista.
    while ( length < 0 ):
        print ( "\n\tLength of the list: " )
        length = int ( input ( "\Respuesta: " ) )
    # Crear una lista de números aleatorios. De lo contrario, una lista en decreciente
    # orden de 'longitud' a 0, en intervalos de 1.
    if ( ans == 1 ):
        gb.n = list ( np.random.randint ( 0, 100, size = length ) )
    else:
        gb.n = list ( range ( length, 0, -1 ) )
        gb.flag = True
    print ( "\n\tList to sort: ", gb.n )