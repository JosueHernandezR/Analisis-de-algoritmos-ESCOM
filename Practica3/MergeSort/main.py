#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 3 Divide y vencerás
# Este es el archivo principal
# Cree un menú para poder elegir cual de los dos algoritmos ejecutar para hacerlo un poco mas sencillo
# Todos los datos son aleatorios
# En el algoritmo de merge, cree dos listas a parte, cada una con diferentes datos y tamaños, para que
# el algoritmo merge trabaje bajo la hipotesis de que lee una lista pero con datos previamente ordenados
# Para evitar cualquier problema, he decidido hacer eso por mi cuenta para que solo el algoritmo se encargue de ordenar las 2 listas

from MergeSort import *
from Merge import *
from grafica import *
import random


def menu():
    ans = 0
    print("\n\n\t\tDivide y vencerás: ")

    while(ans != 1 and ans != 2):
        print("\n\t1.-Usar Merge-Sort")
        print("\t2.-Usar Merge")
        ans = int(input("\tResponder [1/2]: "))
    return ans

def generateMergeSortList():
    mergelist = []
    i = int(random.random()*100)

    for i in range(0,i):
        a = int(random.random()*100)
        mergelist.append(a)
    print("\tLista a ordenar: ", mergelist)
    return mergelist


def generateMergeList():
    #Genera tamaño de listas
    a = int(random.random()*10)
    b = int(random.random()*10)
    #Crea lista
    a_list=[]
    b_list=[]

    for a in range(0,a):
        ar = int(random.random()*100)
        a_list.append(ar)
    ap=sorted(a_list)

    for b in range(0,b):
        br = int(random.random()*100)
        b_list.append(br)
    bp=sorted(b_list)

    lista = ap + bp
    print("\tLista a ordenar: ",lista)
    print("\tLas siguientes listas son con lo que trabajará el algoritmo Merge")
    print("\tLista 1: ", ap)
    print("\tLista 2: ", bp)

    return ap, bp

def main():
    ans = menu()
    if (ans == 2):
        a_list=[]
        b_list=[]
        a_list, b_list = generateMergeList()
        resultado, parametros = onlymerge(a_list, b_list)
        print("\tLista ordenada: ", resultado)
        print("\tParametros (tamaño, tiempo): ", parametros)
        print(type(parametros))
        x, y = parametros
        temp =int( y/x )
        graficaMerge(parametros, temp)
        
    else: 
        mergelist = generateMergeSortList()
        print("Tamaño: ", len(mergelist))
        i=0
        param = []
        for i in range(len(mergelist)+1):
            m, parametros=merge_sort(mergelist[:i])
            param.append(parametros)

        #Lista
        print("\tLista ordenada:", m)
        #(Tamaño de la lista, tiempo)
        print("\tParametros (tamaño, tiempo): ", param)
        graficaMergeSort(param)
main()