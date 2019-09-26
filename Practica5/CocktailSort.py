import global_variables as gb

class CocktailSort:
    # Clase constructor.
    def __init__ ( self, dimensions, start, end ):
        assert len ( dimensions ) > 1
        self.dimensions = dimensions
        self.n = len ( dimensions )
        self.swapped = True
        self.start = start
        self.end = end

    def cocktail ( self ):
        gb.time += 1
        while ( self.swapped ):
            # Restablezca el indicador intercambiado porque podría ser cierto en la próxima iteración.
            gb.time += 1
            self.swapped = False

            # Bucle de izquierda a derecha.
            gb.time += 1
            for i in range ( self.start, self.end ):
                gb.time += 1
                if ( self.dimensions [ i ] > self.dimensions [ i + 1 ] ):
                    gb.time += 4
                    aux = self.dimensions [ i ]
                    self.dimensions [ i ] = self.dimensions [ i + 1 ]
                    self.dimensions [ i + 1 ] = aux
                    self.swapped = True

            # Si no se movió nada, se ordena la matriz.
            gb.time += 1
            if ( self.swapped == False ):
                break
            # De lo contrario, restablezca la bandera para que pueda usarse en la siguiente etapa.
            gb.time += 1
            self.swapped = False
            # Mueva el extremo hacia atrás en una unidad, porque el bucle anterior 
            # movió el número mayor a su lugar correcto.
            gb.time += 1
            self.end = self.end - 1

            # Bucle de derecha a izquierda.
            gb.time += 1
            for i in range ( self.end - 1, self.start - 1, -1 ):
                gb.time += 1
                if ( self.dimensions [ i ] > self.dimensions [ i + 1 ] ):
                    gb.time += 4
                    aux = self.dimensions [ i ]
                    self.dimensions [ i ] = self.dimensions [ i + 1 ]
                    self.dimensions [ i + 1 ] = aux
                    self.swapped = True

            # Aumente el punto de partida, porque el bucle anterior 
            # movió el siguiente número más pequeño a su lugar correcto.
            gb.time += 1
            self.start = self.start + 1
        return self.dimensions
