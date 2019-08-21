#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 1 Suma Binaria
# En este archivo viene el algoritmo de Suma Binaria



def binarysum ( a, b ):
    i, carry, c, count = ( len ( a ) - 1 ), 0, [ ], 1
    # Evalúa ambas listas binarias ('a' y 'b') y desplace desde (n - 1) hasta 0 y suma los números en la posición 'i', el resultado se almacena en 'c'.
    while ( i >= 0 ):
        count += 1
        if ( ( a [ i ] + b [ i ] + carry ) == 1 ):
            count += 1
            c.insert ( 0, 1 )
            count += 1
            carry = 0
            count += 1
        elif ( ( a [ i ] + b [ i ] + carry ) == 2 ):
            count += 1
            c.insert ( 0, 0 )
            count += 1
            carry = 1
            count += 1
        elif ( ( a [ i ] + b [ i ] + carry ) == 3 ):
            count += 1
            c.insert ( 0, 1 )
            count += 1
            carry = 1
            count += 1
        else:
            count += 1
            c.insert ( 0, 0 )
            count += 1
            carry = 0
            count += 1
        i = i - 1
        count += 1
    count += 1
    # Después de terminar, evalúa si hay un valor de acarreo.
    count += 1
    if ( carry == 1 ):
        c.insert ( 0, carry )
        count += 1
    # Return valores.
    return c, count