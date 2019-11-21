#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 10

from deco import *
import pickle
import ast

def getParameters ( ):
    # Obtener la secuencia binaria comprimida.
    compressed = pickle.load ( open ( "../Codificar/Files/Encoded File.txt", "rb" ) )
    # Obtenga el diccionario con la codificación de cada símbolo.
    f = open ( "../Codificar/Files/Dictionary.dic", "r" )
    dictionary = f.read ( )
    dictionary = ast.literal_eval ( dictionary )
    aux = { }
    for key, element in dictionary.items ( ):
        aux [ element ] = key
    f.close ( )
    return compressed, aux

def main ( ):
    compressed, dictionary = getParameters ( )
    decompressed = decode ( dictionary, compressed )
    with ( open ( "Files/Decoded File.txt", "w" ) ) as f:
        f.write ( decompressed )

if ( __name__ == "__main__" ):
    main ( )