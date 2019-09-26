from HeapSort import heapSort
from ShellSort import shellSort
from CombSort import combsort
from grafica import graphHeapSort, graphshellSort, graphcombSort

# Driver code to test above 
arr = [54,26,93,17,77,31,44,55,20]
arreglo, t = heapSort(arr)
arreglo2, t2 = shellSort(arr)
arreglo3, t3 = combsort(arr)
n = len(arr) 
print ("Sorted array is", arreglo)
print("Tiempo heapSort", t)
print("Tiempo shellSort", t2) 
print("Tiempo heapSort", t3)  
# This code is contributed by Mohit Kumra 
graphHeapSort(t, n)
graphshellSort(t2, n)
graphcombSort(t3, n)