# Generador Fibonacci.
def fibonacci ( ):
    a, b = 1, 1
    while ( True ):
        #yield:Se usa para retornar "generators", objetos iteradores que se comportan de manera muy similar a una lista.
        yield a
        a, b = b, a + b

# Lista.
def fibolist ( limit ):
    n, fibo = 0, [ ]
    # Crea una lista de números de Fibonacci usando un generador.
    for i in fibonacci ( ):
        if ( n >= limit ): break
        fibo.append ( i )
        n += 1
    # Devolución.
    return fibo