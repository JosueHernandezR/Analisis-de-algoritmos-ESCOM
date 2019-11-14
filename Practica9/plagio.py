#Análisis de Algoritmos 3CV2
# Alan Romero Lucero
# Josué David Hernández Ramírez
# Práctica 9
import collections
def lcs(s1, s2):

    # Crea listas a partir de los textos introducidos.
    tokens1, tokens2 = s1.split(), s2.split()
    cache = collections.defaultdict(dict)
    # Empieza a crear las matrices
    for i in range(-1, len(tokens1)):
        for j in range(-1, len(tokens2)):
            if i == -1 or j == -1:
                cache[i][j] = 0
            else:
                if tokens1[i] == tokens2[j]:
                    cache[i][j] = cache[i - 1][j - 1] + 1
                else:
                    #Devuelve el elemento más grande
                    cache[i][j] = max(cache[i - 1][j], cache[i][j - 1])
    
    return cache[len(tokens1) - 1][len(tokens2) - 1]

# Lee y guarda el texto de los archivos en una variable
file1=open("prueba51.txt","r")
text1=file1.read()

file2=open("prueba52.txt","r")
text2=file2.read()
# Ejecución de las funciones
original = len(text1.split())
copia = lcs(text1,text2)
print("El número de palabras similares son: ",copia)

# Calculo del porcentaje
porcentaje = float((copia*100)/original)
print("El porcentaje de plagio es: ",round(porcentaje,2), "%")