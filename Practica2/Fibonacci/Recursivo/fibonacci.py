#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Fibonacci Recursivo
# Este es el algoritmo de fibonacci de manera recursiva
def fibonacci ( n, count ):
    count += 1
    if ( n == 1 or n == 2 ):
        return 1, count
    else:
        a, count = fibonacci ( n - 1, count )
        b, count = fibonacci ( n - 2, count )
        return a + b, count