#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 4 Divide y vencerás

from partition import partition
import gb

def quicksort ( n, p, r ):
    gb.time += 1
    if ( p < r ):
        q = partition ( n, p, r )
        gb.time += 1
        quicksort ( n, p, q - 1 )
        gb.time += 1
        quicksort ( n, q + 1, r )
        gb.time += 1