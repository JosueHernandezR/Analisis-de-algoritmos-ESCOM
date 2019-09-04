from MergeSort import *
import random
mergelist = []
i = int(random.random()*1000)
print (i)

for i in range(0,i):
    a = int(random.random()*1000)
    mergelist.append(a)
print(mergelist)
print(len(mergelist))
resultado = merge_sort(mergelist)
print(resultado)

a = int(random.random()*10)
b = int(random.random()*10)

a_list=[]
b_list=[]

for a in range(0,a):
    ar = int(random.random()*100)
    a_list.append(ar)
print(a_list)
ap=sorted(a_list)
print(ap)
for b in range(0,a):
    br = int(random.random()*100)
    b_list.append(br)
print(b_list)
bp=sorted(b_list)
print(bp)


prueba = merge(ap, bp)
print(prueba)