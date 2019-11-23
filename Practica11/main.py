import grafica as plt
import global_variables as gb

def printer ( flag, C ):
    if ( flag == -1 ):
        print ( "\n\n\tLa solución {} no es un ciclo hamiltoniano.\n".format ( C ) )
        exit ( 0 )
    print ( "\n\n\tLa solucion {} es un ciclo hamiltoniano.\n".format ( C ) )

def verify_hamiltonian ( graph, certificate ):
    gb.t += 1
    for i in range ( len ( graph ) ):
        gb.t += 1
        vecinos = graph [ certificate [ i ] ]
        gb.t += 1
        if ( certificate [ i + 1 ] not in vecinos ):
            printer ( -1, certificate )
        gb.parametros.append ( ( len ( certificate [ : i ] ), gb.t + vecinos.index ( certificate [ i + 1 ] ) + 1 ) )
    printer ( 0, certificate )
    print ( gb.parametros )

def main ( ):
    graph = { 1 : [ 20 , 2 , 5 ] , 2 : [ 1 , 18 , 3 ] , 3 : [ 2 , 16 , 4 ] , 4 : [ 3 , 5 , 14 ] ,
            5 : [ 4 , 6 , 1 ] , 6 : [ 5 , 13 , 7 ] , 7 : [ 8 , 6 , 20 ] , 8 : [ 7 , 9 , 12 ] ,
            9 : [ 8 , 19 , 10 ] , 10: [ 9 , 17 , 11 ] , 11: [ 10 , 15 , 12 ] , 12: [ 8 , 13 , 11 ] ,
            13: [ 12 , 6 , 14 ] , 14: [ 13 , 4 , 15 ] , 15: [ 14 , 11 , 16 ] , 16: [ 15 , 17 , 3 ] ,
            17: [ 10 , 16 , 18 ] , 18: [ 17 , 2 , 19 ] , 19: [ 9 , 18 , 20 ] , 20: [ 1 , 19 , 7 ]
    }
    certificate = [ 8 , 9 , 10 , 11 , 12 , 13 , 14 , 15 , 16 , 17 ,
                    18 , 19 , 20 , 1 , 2 , 3 , 4 , 5 , 6 , 7 , 8 ]

    verify_hamiltonian ( graph, certificate )
    plt.plot ( )

if ( __name__ == "__main__" ):
    main ( )