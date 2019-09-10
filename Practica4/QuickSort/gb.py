"""
            MÓDULOS DE VARIABLES GLOBALES
    _parameters: Lista que almacena los parámetros de los puntos a trazar 
        para Partition. Cada elemento es una tupla que almacena la longitud 
        de la lista ordenada y el tiempo que tardó el algoritmo en ejecutar 
        su proceso la primera vez que se llamó.

    parámetros: Lista que almacena los parámetros de los puntos a trazar 
        para Quicksort. Cada elemento es una tupla que almacena la longitud 
        de la lista ordenada y el tiempo que tarda el algoritmo en ordenarla.

    _time: Contador que almacena el tiempo computacional que el algoritmo 
        Partición tarda en finalizar su proceso de ejecución.

    time: Contador que almacena el tiempo computacional que el algoritmo 
        Quicksort toma para ordenar la lista 'n'.

    flag: bandera utilizada en graph.py, ayuda a crear las etiquetas de 
        la función propuesta, dependiendo de si el usuario selecciona 
        el peor o el caso al azar.
    n: Lista para ordenar.
"""

_parameters = [ ( 0, 6 )]
parameters = [ ]
flag = False
_time = 0
time = 0
n = [ ]