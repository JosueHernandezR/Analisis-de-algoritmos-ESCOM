import gb

def shellSort(alist):
    gb._time = 0
    sublistcount = len(alist)//2
    gb._time += 1
    print("Antes del while: ", gb._time)
    while sublistcount > 0:
        gb._time += 1
        print("Antes del for: ", gb._time)
        for startposition in range(sublistcount):
            gb._time += 1
            t, lista = gapInsertionSort(alist,startposition,sublistcount)
            gb._time += 1 + t
        print("After increments of size",sublistcount,
                                    "The list is",lista)

        sublistcount = sublistcount // 2
        gb._time += 1
    return lista, gb._time

def gapInsertionSort(alist,start,gap):
    for i in range(start+gap,len(alist),gap):
        gb._time = 1
        currentvalue = alist[i]
        gb._time += 1
        position = i
        gb._time += 1
        while position>=gap and alist[position-gap]>currentvalue:
            gb._time += 1
            alist[position]=alist[position-gap]
            gb._time += 1
            position = position-gap
            gb._time += 1
        gb._time += 1
        alist[position]=currentvalue
        gb._time += 1
        return gb._time, alist
alist = [54,26,93,17,77,31,44,55,20]
lista, t = shellSort(alist)
print(lista)
print(t)