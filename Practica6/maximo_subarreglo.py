#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 6 Divide y vencerás


"""
Descripción: implementa el método __main__ y contiene 2 funciones:
     Impresora: muestra en pantalla los resultados del proceso de algoritmos.
     crear: crea la matriz de entrada.
Comentarios: Como método adicional, también de las líneas 77 a 91 escribe en un
               presentar el código de látex para las tablas de los puntos de parámetros.
"""

import variablesglobales as gb

def fuerza_bruta ( A ):
    gb.tiempo += 1
    sums = [ 0 ]
    gb.tiempo += 1
    for i in A:
        gb.tiempo += 1
        sums.append ( sums [ -1 ] + i )
        gb.tiempo += 1
    gb.tiempo += 1
    max_sum = int ( -1e100 )
    gb.tiempo += 1
    left_index = -1
    gb.tiempo += 1
    right_index = -1
    gb.tiempo += 1
    for i in range ( len ( A ) ):
        gb.tiempo += 1
        for j in range ( i, len ( A ) ):
            gb.tiempo += 1
            if ( sums [ j + 1 ] - sums [ i ] > max_sum ):
                gb.tiempo += 1
                max_sum = sums [ j + 1 ] - sums [ i ]
                gb.tiempo += 1
                left_index = i
                gb.tiempo += 1
                right_index = j
                gb.tiempo += 1
            gb.tiempo += 1
        gb.tiempo += 1
    # Return statement.
    gb.tiempo += 1
    return left_index, right_index, max_sum

def crossing ( A, low, mid, high ):
    gb.tiempo += 1
    max_left, max_right = 0, 0
    gb.tiempo += 1
    left_sum = int ( -1e100 )
    gb.tiempo += 1
    _sum = 0
    gb.tiempo += 1
    for i in range ( mid - 1, low - 1, -1 ):
        gb.tiempo += 1
        _sum = _sum + A [ i ]
        gb.tiempo += 1
        if ( _sum > left_sum ):
            gb.tiempo += 1
            left_sum = _sum
            gb.tiempo += 1
            max_left = i
        gb.tiempo += 1

    gb.tiempo += 1
    right_sum = int ( -1e100 )
    gb.tiempo += 1
    _sum = 0
    gb.tiempo += 1
    for i in range ( mid, high ):
        gb.tiempo += 1
        _sum = _sum + A [ i ]
        gb.tiempo += 1
        if ( _sum > right_sum ):
            gb.tiempo += 1
            right_sum = _sum
            gb.tiempo += 1
            max_right = i
        gb.tiempo += 1
    # Return statement.
    gb.tiempo += 1
    return max_left, max_right, right_sum + left_sum

def recurrencia ( A, low, high ):
    gb.tiempo += 1
    if ( high == low + 1 ):
        gb.tiempo += 1
        return low, high, A [ low ]
    else:
        gb.tiempo += 1
        mid = int ( ( low + high ) / 2 )
        gb.tiempo += 1
        left_low, left_high, left_sum = recurrencia ( A, low, mid )
        gb.tiempo += 1
        right_low, right_high, right_sum = recurrencia ( A, mid, high )
        gb.tiempo += 1
        cross_low, cross_high, cross_sum = crossing ( A, low, mid, high )
        gb.tiempo += 1
        if ( left_sum >= right_sum and left_sum >= cross_sum ):
            gb.tiempo += 1
            return left_low, left_high, left_sum
        elif ( right_sum >= left_sum and right_sum >= cross_sum ):
            gb.tiempo += 1
            return right_low, right_high, right_sum
        else:
            gb.tiempo += 1
            return cross_low, cross_high, cross_sum