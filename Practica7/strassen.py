"""
Descrición: Implementación del algoritmo de Strassen
"""

from operaciones_matrices import *
import variables_globales as gb
from sub_matrices import *

def strassen ( A, B ):
    # Valida la condición de matrices de tamaño [2 ^ n x 2 ^ n].
    assert len ( A ) == len ( A [ 0 ] ) == len ( B ) == len ( B [ 0 ] )
    assert type ( A ) == list and type ( B ) == list

    # Producto matricial habitual.
    gb.time += 1
    if ( len ( A ) == 1 ):
        gb.time += 1
        return [ [ A [ 0 ] [ 0 ] * B [ 0 ] [ 0 ] ] ]
    else:
    # Algoritmo de Strassen.
        gb.time += 1
        n = int ( len ( A ) / 2 )
        gb.time += 1
        # Divide las matrices A y B en octavas submatrices de tamaño 2 ^ n / 2.
        A11, A12, A21, A22, B11, B12, B21, B22 = split_in_sub_matrices ( A, B, n )
        gb.time += 1
        # S1 = strassen ( ( A11 + A22 ), ( B11 + B22 ) )
        S1 = strassen ( suma ( A11, A22 ), suma ( B11, B22 ) )
        gb.time += 1
        # S2 = strassen ( ( A21 + A22 ), ( B11 ) )
        S2 = strassen ( suma ( A21, A22 ), B11 )
        gb.time += 1
        # S3 = strassen ( ( A11 ), ( B12 - B22 ) )
        S3 = strassen ( A11, resta ( B12, B22 ) )
        gb.time += 1
        # S4 = strassen ( ( A22 ), ( B21 - B11 ) )
        S4 = strassen ( A22, resta ( B21, B11 ) )
        gb.time += 1
        # S5 = strassen ( ( A11 + A12 ), ( B22 ) )
        S5 = strassen ( suma ( A11, A12 ), B22 )
        gb.time += 1
        # S6 = strassen ( ( A21 - A11 ), ( B11 + B12 ) )
        S6 = strassen ( resta ( A21, A11 ), suma ( B11, B12 ) )
        gb.time += 1
        # S7 = strassen ( ( A12 - A22 ), ( B21 + B22 ) )
        S7 = strassen ( resta ( A12, A22 ), suma ( B21, B22 ) )

        # Expresando Cij en términos de Sk, donde C es la matriz resultante.
        gb.time += 1
        # C11 = S1 + S4 - S5 + S7
        C11 = resta ( suma ( suma ( S1, S4 ), S7 ), S5 )
        gb.time += 1
        # C12 = S3 + S5
        C12 = suma ( S3, S5 )
        gb.time += 1
        # C21 = S2 + S4
        C21 = suma ( S2, S4 )
        gb.time += 1
        # C22 = S1 - S2 + S3 + S6
        C22 = suma ( resta ( S1, S2 ), suma ( S3, S6 ) )
        # Unir todas las submatrices resultantes
        gb.time += 1
        return join_sub_matrices ( C11, C12, C21, C22, n * 2 )