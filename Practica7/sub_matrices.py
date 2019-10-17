#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 7 Strassen


"""
Descripción: implementa dos métodos:
     split_in_sub_matrices: divide las matrices de entrada en submatrices de tamaño n / 2 x n / 2.
     join_sub_matrices: une 4 submatrices de tamaño n / 2 x n / 2 en una matriz resultante.
"""

def split_in_sub_matrices ( A, B, n ):
    # Inicializar las submatrices.
    A11, A12, A21, A22 = [ ], [ ], [ ], [ ]
    B11, B12, B21, B22 = [ ], [ ], [ ], [ ]
    # Rellene las submatrices.
    for i in range ( n ):
        A11.append ( A [ i ] [ :n ] )
        A12.append ( A [ i ] [ n: ] )
        A21.append ( A [ n + i ] [ :n ] )
        A22.append ( A [ n + i ] [ n: ] )
        B11.append ( B [ i ] [ :n ] )
        B12.append ( B [ i ] [ n: ] )
        B21.append ( B [ n + i ] [ :n ] )
        B22.append ( B [ n + i ] [ n: ] )
    # Declaración de devolución.
    return A11, A12, A21, A22, B11, B12, B21, B22

def join_sub_matrices ( C11, C12, C21, C22, n ):
    C, sub_size = [ ], int ( n / 2 )
    for i in range ( sub_size ):
        C.append ( C11 [ i ] + C12 [ i ] )
    for i in range ( sub_size ):
        C.append ( C21 [ i ] + C22 [ i ] )
    # Declaración de devolución.
    return C