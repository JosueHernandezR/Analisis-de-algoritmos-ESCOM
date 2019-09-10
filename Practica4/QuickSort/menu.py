import numpy as np
import gb

def menu ( ):
    ans, length = -1, -1
    # Opción de menú 1: el usuario debe seleccionar si crear una lista de números aleatorios o
    # una lista en el peor de los casos para el algoritmo, ordenada en orden decreciente.
    while ( ans != 1 and ans != 2 ):
        print ( "\n\n\t\t\tQUICK-SORT\n\n\t Select one of the following options." )
        print ( "\n\t1.- Random case." )
        print ( "\t2.- Worst case." )
        ans = int ( input ( "\tAnswer: " ) )
    # Opción de menú 2: el usuario debe elegir la longitud de la lista.
    while ( length < 0 ):
        print ( "\n\tLength of the list: " )
        length = int ( input ( "\tAnswer: " ) )
    # Crear una lista de números aleatorios. De lo contrario, una lista en decreciente
    # orden de 'longitud' a 0, en intervalos de 1.
    if ( ans == 1 ):
        gb.n = list ( np.random.randint ( 0, 100, size = length ) )
    else:
        gb.n = list ( range ( length, 0, -1 ) )
        gb.flag = True
    print ( "\n\tList to sort: ", gb.n )