
from grafica import grafica
from cubo import cubo

def main ( ):
    n = int ( input ( "\n\tNumber to calculate firts n-Cubes: " ) )
    # cube ( n ): Return the _sum of the first 'n' cubes, the computational time
    # of the algorithm and a list of the sum of nth cubes.
    _sum, count, cubelist = cubo ( n )
    print ( "\n\tThe sum of the first ", n, " cubes is: C ( ", n, " ) = ", _sum, "\n" )
    grafica ( _sum, count, cubelist, n )
main ( )