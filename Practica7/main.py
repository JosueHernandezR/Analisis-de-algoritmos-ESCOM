import variables_globales as gb
from crear_matrices import *
from producto_ijk import *
from strassen import *
from plot import *

def printer ( A, B, C ):
    # Validates the condition of matrices of [ 2^n x 2^n ] size.
    assert len ( A ) == len ( B ) == len ( C )

    print ( "\n\tAlgoritmo de Strasen:" )
    print ( "\n\Matriz A:\n" )
    list ( map ( lambda x: print ( "\t{}".format ( x ) ), A ) )
    print ( "\n\Matriz B:\n" )
    list ( map ( lambda x: print ( "\t{}".format ( x ) ), B ) )
    print ( "\n\Producto A * B:\n" )
    list ( map ( lambda x: print ( "\t{}".format ( x ) ), C ) )
    n = len ( C )
    print ( "\n\Donde: A, B, C ∈ M [ {}x{} ] ( ℤ+ )".format ( n, n ) )
    print ( "\n\tParámetros del algoritmo de Strassen: {}\n".format ( gb.parametros ) )
    if ( gb.flag == True ):
        print ( "\tParámetros del algoritmo IJK: {}\n".format ( gb._parametros ) )


if ( __name__ == "__main__" ):
    power = int ( input ( "\n\tAgregar una enésima potencia: " ) )
    if ( power >= 8 ):
        gb.flag = True
    for i in range ( 1, power + 1 ):
        # Strassen algorithm.
        n = int ( math.pow ( 2, i ) )
        A, B = create ( n )
        C = strassen ( A, B )
        gb.parametros.append ( ( n, gb.time ) )
        gb.time = 0
        # Para una matriz grande, compare el algoritmo de Strassen con el algoritmo ijk.
        if ( gb.flag == True ):
            _C = producto_ijk ( A, B )
            gb._parametros.append ( ( n, gb._time ) )
            gb._time = 0
    printer ( A, B, C )
    plot ( )