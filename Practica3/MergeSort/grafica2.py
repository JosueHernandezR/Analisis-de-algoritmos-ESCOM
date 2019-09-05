import matplotlib.pyplot as plt
import numpy as np
def graficaMerge(parametros, temp):
    plt.figure("Algoritmo Merge")
    plt.title("Merge (tamaño, tiempo) = (" + str(parametros[0] + "," + str(pametros[1] + 1) + ")")

    t = np.arange(0, parametros[1] + 1, temp)
    n = np.arange(0, parametros[0]+1)
    _t = list(map(lambda x : (5/2)* x, t))

    # Nombres de los ejes
    plt.xlabel("Tamaño (n)", color="red")
    plt.ylabel("Tiempo(t)", color="blue")

    #Graficar
    plt.plot(n, t, "bo-", label="T(n)=(n)(log (n))")
    plt.plot(n, _t, "ro-", label="g(n)=(5/2)(n)(log (n))")
    plt.legend(loc="upper left")
    plt.show()