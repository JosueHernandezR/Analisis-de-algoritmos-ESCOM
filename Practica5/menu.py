import numpy as np

def menu():
    ans, length = -1, -1
    while (ans != 1 and ans !=2  and ans != 3):
        print("\n\n\t\t\tSelecciona algunas de las siguientes opciones")
        print("\n\t1.- Mejor de los casos.")
        print("\n\t2.- Casos aleatorios.")
        print("\n\t3.- Peor de los casos.")
        ans = int(input("\n\tRespuesta:"))

    
    