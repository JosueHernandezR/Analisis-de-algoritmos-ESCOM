##
# Python's algorithm of Combsort sort
import gb 
 
def combsort(num):
    gb.time = 0
    gap = len(num)
    gb.time += 1
    swaps = True
    gb.time += 1
    while gap > 1 or swaps:
        gb.time += 1
        gap = max(1, int(gap / 1.25))  # minimum gap is 1
        gb.time += 1
        swaps = False
        gb.time += 1
        for i in range(len(num) - gap):
            gb.time += 1
            j = i+gap
            gb.time += 1
            if num[i] > num[j]:
                gb.time += 1
                num[i], num[j] = num[j], num[i]
                gb.time += 1
                swaps = True
                gb.time += 1
    print("Num", num)
    print("Time: ", gb.time)
    return num, gb.time


alist = [54,26,93,17,77,31,44,55,20]
lista, t = combsort(alist)
print(lista)
print(t)