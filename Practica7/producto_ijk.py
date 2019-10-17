#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 7 Strassen

import variables_globales as gb

def producto_ijk ( A, B ):
    # Valida la condición de matrices de tamaño [2 ^ n x 2 ^ n].
    assert len ( A ) == len ( A [ 0 ] ) == len ( B ) == len ( B [ 0 ] )
    assert type ( A ) == list and type ( B ) == list

    gb._time += 1
    n = len ( A )
    gb._time += 1
    C = [ [ 0 for i in range ( n ) ] for j in range ( n ) ]
    gb._time += 1
    for i in range ( n ):
        gb._time += 1
        for j in range ( n ):
            gb._time += 1
            for k in range ( n ):
                gb._time += 1
                C [ i ] [ j ] += A [ i ] [ k ] * B [ k ] [ j ]
                gb._time += 1
            gb._time += 1
        gb._time += 1
    gb._time += 1
    # Declaración de devolución.
    gb._time += 1
    return C