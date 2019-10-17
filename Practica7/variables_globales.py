#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 7 Strassen

"""
Descripción: este módulo solo almacena las variables globales del programa:
        parámetros: Lista que almacena los parámetros de los puntos a trazar para el algoritmo de
                    Strassen. Cada elemento es una tupla que almacena la longitud del
                    matrices y el tiempo que tarda el algoritmo en calcular el producto.
        time: Contador que almacena el tiempo computacional que tarda el algoritmo de Strassen en
                    calcular el producto de dos matrices.
        _parameters: Lista que almacena los parámetros de los puntos a trazar para el algoritmo ijk
                    es una tupla que almacena la longitud de las matrices y el tiempo que
                    el algoritmo tarda en calcular el producto.
        _time: Contador que almacena el tiempo de cálculo que tarda el algoritmo ijk en calcular
                    el producto de dos matrices.
        Bandera: Almacena un booleano, se usa en plot.py, si el tamaño de las matrices es mayor o igual a 2 ^ 8
                    entonces, Flag tomará el valor de "verdadero" y el programa comparará la complejidad de
                    el algoritmo de Strassen contra el producto matricial habitual (algoritmo ijk).
"""

_parametros = [ ]
parametros = [ ]
flag = False
_time = 0
time = 0