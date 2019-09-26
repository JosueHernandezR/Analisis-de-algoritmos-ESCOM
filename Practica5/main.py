import global_variables as gb
from HeapSort import *
from CocktailSort import *
from ShellSort import *
from grafica import *
import random as rnd

def menu ( ):
    print ( "\n\n\tAlgoritmos de clasificación: seleccione una de las siguientes opciones." )
    print ( "\n\t1.- Heap-Sort." )
    print ( "\t2.- Cocktail-Sort." )
    print ( "\t3.- Shell-Sort.")
    return int ( input ( "\tRespuesta: " ) )

def printer_1 ( dimensions, j ):
    if ( j == 0 ):
        case = "Mejor caso:"
    if ( j == 1 ):
        case = "Caso aleatorio:"
    if ( j == 2 ):
        case = "Peor caso:"
    print ( "\n\t{}\n\n\tList to sort: {}".format ( case, dimensions ) )

def printer_2 ( dimensions ):
    print ( "\n\tSorted List:  {}\n".format ( dimensions ) )

if ( __name__ == "__main__" ):
    ans, j = menu ( ), 0
    while ( j < 3 ):
        # Mejor, aleatorio y peor caso de cada algoritmo.
        if ( j == 0 ):
            dimensions = [ i for i in range ( 0, 50 ) ]
        if ( j == 1 ):
            dimensions = [ rnd.randint ( 0, 50 ) for i in range ( 50 ) ]
        if ( j == 2 ):
            dimensions = [ i for i in range ( 50, 0, -1 ) ]
        printer_1 ( dimensions, j )
        # Ordena las dimensiones de la lista.
        for i in range ( 2, len ( dimensions ) + 1 ):
            if ( ans == 1 ):
                algorithm = HeapSort ( dimensions [ :i ] )
                sort = algorithm.heapsort ( )
            if ( ans == 2 ):
                algorithm = CocktailSort ( dimensions [ :i ], 0, len ( dimensions [ :i ] ) - 1 )
                sort = algorithm.cocktail ( )
            if ( ans == 3 ):
                algorithm = ShellSort ( dimensions [ :i ] )
                sort = algorithm.shellsort ( )
            if ( j == 0 ):
                gb.parameters_1.append ( ( len ( dimensions [ :i ] ), gb.time ) )
            if ( j == 1 ):
                gb.parameters_2.append ( ( len ( dimensions [ :i ] ), gb.time ) )
            if ( j == 2 ):
                gb.parameters_3.append ( ( len ( dimensions [ :i ] ), gb.time ) )
            gb.time = 0
        j = j + 1
        printer_2 ( sort )
    plot ( ans )