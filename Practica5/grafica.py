import matplotlib.pyplot as plt
import numpy as np

def graphHeapSort(t, tam):
    plt.figure("Algoritmo HeapSort")
    
    plt.title("Algoritmo HeapSort")
    
    tiempo = np.arange(0, t, (t / tam))
    _tiempo = list(map((lambda x: x * (5/2)) ,tiempo))
    _tam = np.arange(0, tam )
    plt.xlabel("Tam")
    plt.ylabel("Time")
    
    plt.plot(_tam, _tiempo, "b^--", label = "g(n) = (5/2)(n)")
    plt.plot(_tam, tiempo, "ro--", label = "T(n) = (n)")
    plt.legend ( loc = "upper left" )
    plt.show()

def graphshellSort(t, tam):
    plt.figure("Algoritmo shellSort")
    
    plt.title("Algoritmo shellSort")
    
    tiempo = np.arange(0, t, (t / tam))
    _tiempo = list(map((lambda x: x * (5/2)) ,tiempo))
    _tam = np.arange(0, tam )
    plt.xlabel("Tam")
    plt.ylabel("Time")
    
    plt.plot(_tam, _tiempo, "b^--", label = "g(n) = (5/2)(n)")
    plt.plot(_tam, tiempo, "ro--", label = "T(n) = (n)")
    plt.legend ( loc = "upper left" )
    plt.show()

def graphcombSort(t, tam):
    plt.figure("Algoritmo combSort")
    
    plt.title("Algoritmo combSort")
    
    tiempo = np.arange(0, t, (t / tam))
    _tiempo = list(map((lambda x: x * (5/2)) ,tiempo))
    _tam = np.arange(0, tam )
    plt.xlabel("Tam")
    plt.ylabel("Time")
    
    plt.plot(_tam, _tiempo, "b^--", label = "g(n) = (5/2)(n)")
    plt.plot(_tam, tiempo, "ro--", label = "T(n) = (n)")
    plt.legend ( loc = "upper left" )
    plt.show()