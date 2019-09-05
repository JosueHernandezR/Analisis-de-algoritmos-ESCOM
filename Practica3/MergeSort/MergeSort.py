import globalvariables as gb


# Función merge_sort


def merge_sort(lista):
    gb.time = 0
    """
    Lo primero que se ve en el psudocódigo es un if que
    comprueba la longitud de la lista. Si es menor que 2, 1 o 0, se devuelve la lista.
    ¿Por que? Ya esta ordenada. 
    """
    if len(lista) < 2:
        return lista, (len(lista), gb.time)
        # De lo contrario, se divide en 2
    else:
        middle = len(lista) // 2
        gb.time += 1
        right, parametros = merge_sort(lista[:middle])
        gb.time += 1 + parametros [1]
        left, parametros = merge_sort(lista[middle:])
        gb.time += 1 + parametros [1]
        m , t = merge(left, right)
        gb.time += 1 + t
        return m, (len(lista), gb.time)
        
# Función merge
def merge(izq, der):
    """
    Merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
    gb.time = 1 #Contador
 
    # Intercalar ordenadamente
    while(i < len(izq) and j < len(der)):
        gb.time += 1
        if (izq[i] < der[j]):
            result.append(izq[i])
            gb.time += 1
            i += 1
            gb.time += 1
        else:
            result.append(der[j])
            gb.time += 1
            j += 1
            gb.time += 1
    gb.time += 1
    # Agregamos los resultados a la lista
    result.extend(izq[i:])
    result.extend(der[j:])
    gb.time += 2
    # Retornamos el resultados
    return result, gb.time
