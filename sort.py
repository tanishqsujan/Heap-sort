def heapsort(arr):
    n= len(arr)
    
    #Build maxheap
    for i in range(n//2 -1, -1, -1):
        heapify(arr, n, i)
        
    #Extract the elements one by one
    for i in range(n-1, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        heapify(arr, i, 0)
        
def heapify(arr, n, i):
    largest = i
    l= 2 * i + 1
    r= 2 * i + 2
    
    #See if left child of root exists and is greater than root
    if l < n and arr[l] > arr[largest]:
        largest = l
    
    #See if right child of root exists and is greater than root    
    if r < n and arr[r] > arr[largest]:
        largest = r
    
    #Change root if needed    
    if largest != i:
        arr[i], arr[largest] = arr[largest], arr[i]#swap
        
        #Heapify the root
        heapify(arr, n, largest)
        
if __name__ == "__main__":
    arr = [12, 11, 13, 5, 6, 7]
    
    #Function call
    heapsort(arr)
    N= len(arr)
    
    print("Sorted array is")
    for i in range(N):
        print("%d" %arr[i], end=" ")