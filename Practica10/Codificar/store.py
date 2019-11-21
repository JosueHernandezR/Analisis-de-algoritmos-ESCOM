#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 10

import pickle
import json

def store ( compressed, frequency, probability, dictionary ):
    # Almacena la secuencia codificada en un archivo binario.
    with ( open ( "Files/Encoded File.txt", "wb" ) ) as f:
        pickle.dump ( compressed, f )
    # Almacena la frecuencia con la que aparecieron los símbolos.
    with ( open ( "Files/Frequency.txt", "w" ) ) as f:
        f.write ( "\n\t\t{0:10} {1:15} {2:10}\n\t\t"
                  .format ( "Symbol", "Probability", "Frequency" ) )
        for symbol in frequency:
            f.write ( "{0:10} {1:15.6} {2:10}\n\t\t"
                      .format ( symbol, str ( probability [ symbol ] ),
                                        str ( frequency [ symbol ] ) ) )
    # Almacena la codificación de cada símbolo.
    with ( open ( "Files/Codification.txt", "w" ) ) as f:
        f.write ( "\n\t\t{0:10} {1:10}\n\t\t"
                  .format ( "Symbol", "Codes" ) )
        for symbol in dictionary:
            f.write ( "{0:10} {1:10}\n\t\t"
                      .format ( symbol, dictionary [ symbol ] ) )
    # Almacena el diccionario con la codificación de cada símbolo.
    with ( open ( "Files/Dictionary.dic", "w" ) ) as f:
        json.dump ( dictionary, f )