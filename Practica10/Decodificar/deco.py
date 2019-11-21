#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 10

def decode ( dictionary, binary ):
    result = [ ]
    length = binary.bit_length ( ) - 1
    # El primer carácter debe ser 1, de lo contrario, hay un error.
    if ( binary >> length != 1 ):
        raise ( "Error: Corrupt file." )
    done = False
    while ( length > 0 and ( not done ) ):
        shift = length - 1
        # Aumentar poco a poco.
        while ( True ):
            num = binary >> shift
            # Eliminar el '1' inicial y el '0b' del formato.
            bitnum = bin ( num ) [ 3: ]
            if ( bitnum not in dictionary ):
                shift -= 1
                continue
            char = dictionary [ bitnum ]
            if ( char == "end" ):
                done = True
                break
            result.append ( char )
            binary = binary - ( ( num - 1 ) << shift )
            length = shift
    return "".join ( result )