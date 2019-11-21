#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 10

from collections import Counter
import heapq

class Huffman:
    # Clase constructor
    def __init__ ( self, txtin ):
        self.probability = { }
        self.frequency = { }
        self.txtin = txtin
        self.codes = { }
        self.txtout = ""
        self.result = ""
        self.tree = [ ]

    # Establecer la frecuencia de aparición de cada símbolo.
    def setFrequency ( self ):
        total = len ( self.txtin ) + 1
        c = Counter ( self.txtin )
        self.probability = {}
        self.frequency = {}
        for char, counter in c.items ( ):
            self.probability [ char ] = float ( counter ) / total
            self.frequency [ char ] = counter
        self.probability [ "end" ] = 1.0 / total
        self.frequency [ "end" ] = 1

    # Crear el árbol de algoritmos de Huffman.
    def setTree ( self ):
        # Agregue los símbolos a la pila de prioridad según los montones.
        for char, freq in self.frequency.items ( ):
            # La pila está ordenada por prioridad y profundidad.
            heapq.heappush ( self.tree, ( freq, 0, char ) )
        # Comience a 'mezclar' símbolos contiguos hasta que la fila tenga un elemento.
        while ( len ( self.tree ) > 1 ):
            # First and second less frequents symbols.
            e1 = heapq.heappop ( self.tree )
            e2 = heapq.heappop ( self.tree )
            node = ( e1 [ 0 ] + e2 [ 0 ], max ( e1 [ 1 ], e2 [ 1 ] ) + 1, [ e1, e2 ] )
            heapq.heappush ( self.tree, node )
        # Devuelve el árbol sin la fila.
        self.tree = self.tree [ 0 ]

    def setCodes ( self ):
        # Profundidad-Primera pila de búsqueda.
        searchStack = [ ]
        searchStack.append ( self.tree + ( "", ) )
        while ( len ( searchStack ) > 0 ):
            element = searchStack.pop ( )
            if ( type ( element [ 2 ] ) == list ):
                # El nodo no es una hoja.
                searchStack.append ( element [ 2 ] [ 1 ] + ( element [ -1 ] + "1", ) )
                searchStack.append ( element [ 2 ] [ 0 ] + ( element [ -1 ] + "0", ) )
            else:
                # El nodo es una hoja.
                code = element [ -1 ]
                self.codes [ element [ 2 ] ] = code
            pass

    def encode ( self ):
        for char in self.txtin:
            code = self.codes [ char ]
            self.result = self.result + code
        # Agregue un 1 a la izquierda y el marcador FIN.
        self.result = "1" + self.result + self.codes [ "end" ]
        self.result = int ( self.result, 2 )