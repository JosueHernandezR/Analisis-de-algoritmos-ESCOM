#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 10

from collections import Counter
from huffman import *
from store import *

TEST = "This is a test for Huffman's algorithm."

def getText ( ):
    with ( open ( "Files/Original.txt", "r" ) ) as f:
        txtin = f.read ( ).rstrip ( "\n" )
        content = TEST if ( txtin == "" ) else txtin
    return content

def main ( ):
    txtin = getText ( )
    huffman = Huffman ( txtin )
    huffman.setFrequency ( )
    huffman.setTree ( )
    huffman.setCodes ( )
    huffman.encode ( )
    store ( huffman.result, huffman.frequency, huffman.probability, huffman.codes )

if ( __name__ == "__main__" ):
    main ( )