#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 2 Suma de las primeras n cúbicas "Iterativo"
#Este es el algoritmo de las sumas de forma iterativa

def cubo ( n ):
    _sum, count, cubelist = 0, 1, [ ]
    # Rango: Desde 1 <= i <= n.
    for i in range ( 1, n + 1 ):
        count += 1
        _sum = _sum + i**3
        count += 1
        cubelist.append ( _sum )
        count += 1
    # Return.
    count += 1
    return _sum, count, cubelist