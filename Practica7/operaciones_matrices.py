#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 7 Strassen

"""
Descripción: Implementaciones de la suma y resta de dos matrices.
"""


def suma ( A, B ):
    n = len ( A )
    C = [ [ A [ i ] [ j ] + B [ i ] [ j ] for j in range ( n ) ] for i in range ( n ) ]
    # Return statement.
    return C

def resta ( A, B ):
    n = len ( A )
    C = [ [ A [ i ] [ j ] - B [ i ] [ j ] for j in range ( n ) ] for i in range ( n ) ]
    # Return statement.
    return C