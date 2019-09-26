import global_variables as gb

class Shell:
    # Class constructor.
    def __init__ ( self, dimensions ):
        assert len ( dimensions ) > 1
        self.dimensions = dimensions
        self.n = len ( dimensions )
        self.gap = int ( self.n / 2 )

    # Algoritmo Shellsort
    def shellsort ( self ):
        # Haga una clasificación de inserción con espacios para el tamaño del espacio. 
        # Los primeros elementos de espacio de las dimensiones [0 .. espacio - 1] ya 
        # están en orden de espacio entonces, continúe agregando un elemento más hasta 
        # que toda la matriz esté ordenada.
        gb.time += 1
        while ( self.gap > 0 ):
            # Agregar dimensiones [i] en los elementos que se han ordenado por huecos.
            gb.time += 1
            for i in range ( self.gap, self.n ):
                # Guarde las dimensiones [i] en la variable 'temp' y haga un agujero 
                # en la posición i.
                gb.time += 1
                temp = self.dimensions [ i ]
                # Desplaza los elementos anteriores ordenados por espacios hacia arriba 
                # hasta encontrar la ubicación correcta para las dimensiones [i].
                gb.time += 1
                j = i
                gb.time += 1
                while ( j >= self.gap and self.dimensions [ j - self.gap ] > temp ):
                    gb.time += 1
                    self.dimensions [ j ] = self.dimensions [ j - self.gap ]
                    gb.time += 1
                    j = j - self.gap
                # Coloca en la variable 'temp' (las dimensiones originales [i]) en su ubicación correcta.
                gb.time += 1
                self.dimensions [ j ] = temp
            gb.time += 1
            self.gap = int ( self.gap / 2 )
        return self.dimensions