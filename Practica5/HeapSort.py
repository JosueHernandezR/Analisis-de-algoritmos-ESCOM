import gb

# Python program for implementation of heap Sort 

# To heapify subtree rooted at index i. 
# n is size of heap 
def heapify(arr, n, i):
    gb.__time = 1 
    largest = i # Initialize largest as root 
    gb.__time += 1
    l = 2 * i + 1	 # left = 2*i + 1
    gb.__time += 1 
    r = 2 * i + 2	 # right = 2*i + 2
    gb.__time += 1 

	# See if left child of root exists and is 
	# greater than root 
    if l < n and arr[i] < arr[l]:
        gb.__time += 1
        largest = l
        gb.__time += 1 
	# See if right child of root exists and is # greater than root 
    if r < n and arr[largest] < arr[r]:
        gb.__time += 1
        largest = r
        gb.__time += 1
	# Change root, if needed 
    if largest != i: 
        gb.__time += 1
        arr[i],arr[largest] = arr[largest], arr[i];
        gb.__time += 1 
        heapify(arr, n, largest); 
        gb.__time += 1
    gb.__time += 1
    return arr, gb.__time
# The main function to sort an array of given size
def heapSort(arr):
	gb.__time = 0 
	n = len(arr)
	gb.__time += 1
	ff, sf, temp = 0, 0, 0

	# Build a maxheap. 
	for i in range(n, -1, -1):
		gb.__time += 1
		arreglo, t = heapify(arr, n, i)
		gb.__time += 1 + t
		arr = arreglo
		gb.__time += 1
		ff = ff + gb.__time
		ff +=1
	gb.__time += 1 + ff
	temp = gb.__time
	print("first for", gb.__time)
	# One by one extract elements 
	for i in range(n-1, 0, -1):
		gb.__time += 1
		arr[i], arr[0] = arr[0], arr[i];
		gb.__time += 1 +temp
		arreglo, t = heapify(arr, i, 0)
		gb.__time += 1 + t
		arr = arreglo
		gb.__time += 1
		sf = sf + gb.__time
		sf += 1
	gb.__time += 1 + sf + temp
	return arr, gb.__time

# Driver code to test above 
arr = [54,26,93,17,77,31,44,55,20]
arreglo, t = heapSort(arr) 
n = len(arr) 
print ("Sorted array is", arreglo)
print("time", t) 
# This code is contributed by Mohit Kumra 
