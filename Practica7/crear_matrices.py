#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 7 Strassen

"""
Descripción: Crea las matrices A y B.
"""

import random as rnd
import math

def create ( n ):
    # Tamaño de las matrices: 2 ^ n.
    A = [ [ rnd.randint ( 0, 9 ) for i in range ( n ) ] for j in range ( n ) ]
    B = [ [ rnd.randint ( 0, 9 ) for i in range ( n ) ] for j in range ( n ) ]
    return A, B