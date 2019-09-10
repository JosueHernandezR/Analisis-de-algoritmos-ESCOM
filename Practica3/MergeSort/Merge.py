#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 3 Divide y vencerás
# Este es el algoritmo usado en merge, ya que los datos que devuelve no son los mismos usados en merge sort
# Esto lo hice para fines prácticos y ahorro de tiempo

import globalvariables as gb

def onlymerge(izq, der):
    """
    Merge se encargara de intercalar los elementos de las dos
    divisiones.
    """
    i, j = 0, 0 # Variables de incremento
    result = [] # Lista de resultado
    gb.time = 0 #Contador
    gb.time += 1
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
    gb.time += 1
    result.extend(der[j:])
    gb.time += 1
    # Retornamos el resultados
    return result, (len(result), gb.time)
