import global_variables as gb

class HeapSort:
    # Clase constructor.
    def __init__ ( self, dimensions ):
        assert len ( dimensions ) > 1
        self.dimensions = dimensions
        self.n = len ( dimensions )

    # Heapify es un subárbol enlazado en el índice i.
    def heapify ( self, i, j ):
        gb.time += 3
        right = 2 * j + 2
        left = 2 * j + 1
        largest = j
        # Verifica si el hijo izquierdo existe y si es mayor que la raíz.
        gb.time += 1
        if ( left < i and self.dimensions [ j ] < self.dimensions [ left ] ):
            gb.time += 1
            largest = left
        # Verifique si el hijo derecho existe y si es mayor que la raíz.
        gb.time += 1
        if ( right < i and self.dimensions [ largest ] < self.dimensions [ right ] ):
            gb.time += 1
            largest = right
        # Cambie la raíz si es necesario.
        gb.time += 1
        if ( largest != j ):
            gb.time += 4
            aux = self.dimensions [ j ]
            self.dimensions [ j ] = self.dimensions [ largest ]
            self.dimensions [ largest ] = aux
            # "Heapify" la raiz.
            self.heapify ( i, largest )

    # Algoritmo Heapsort,
    def heapsort ( self ):
        # Construye el moontículo máximo.
        gb.time += 1
        for i in range ( self.n, -1, -1 ):
            gb.time += 1
            self.heapify ( self.n, i )
        # Extrae los elementos uno por uno.
        gb.time += 1
        for i in range ( ( self.n - 1 ), 0, -1 ):
            gb.time += 4
            aux = self.dimensions [ i ]
            self.dimensions [ i ] = self.dimensions [ 0 ]
            self.dimensions [ 0 ] = aux
            self.heapify ( i, 0 )
        return self.dimensions