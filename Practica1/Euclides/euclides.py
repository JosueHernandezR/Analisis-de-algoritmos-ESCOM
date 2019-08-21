#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Algoritmo de Euclides
# Este archivo contiene el algoritmo de Euclides con el MCD

def algoritmo ( n, m ):
    # Algoritmo euclidiano: encuentra el divisor común más grande (mcd).
    count, mcd = 1, [ ]
    while ( m != 0 ):
        mcd.append ( n )
        count += 1
        r = n % m
        count += 1
        n = m
        count += 1
        m = r
        count += 1
    count += 1
    # Declaración de devolución.
    return n, count, mcd