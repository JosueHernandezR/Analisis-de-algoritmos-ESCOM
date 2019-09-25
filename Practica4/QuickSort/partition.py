#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 4 Divide y vencerás

import gb

def partition ( n, p, r ):
    x = n [ r ] # pivot
    gb._time += 1
    i = p # border
    gb._time += 1
    for j in range ( p, r ):
        gb._time += 1
        if ( n [ j ] < x ):
            aux = n [ j ]
            gb._time += 1
            n [ j ] = n [ i ]
            gb._time += 1
            n [ i ] = aux
            gb._time += 1
            i += 1
            gb._time += 1
    gb._time += 1
    aux = n [ i ]
    gb._time += 1
    n [ i ] = n [ r ]
    gb._time += 1
    n [ r ] = aux
    gb._time += 1
    # Suma la complejidad temporal de la Partición '_time' a la temporal
    # complejidad de Quicksort 'time'.
    gb.time += gb._time
    if ( r > gb._parameters [ len ( gb._parameters ) - 1 ][ 0 ] ):
        gb._parameters.append ( ( r, gb._time ) )
    gb._time = 0
    return i