def bubble(arr):
    n = len(arr)
    for i in range(1,n):
        for j in range(0,n-i):
            if arr[j]>arr[j+1]:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    print(arr)
    return

def selection(arr):
    n = len(arr)
    for i in range(n):
        mini = i
        for j in range(i+1,n):
            if arr[j]<arr[mini]:
                mini = j
        arr[i],arr[mini] = arr[mini],arr[i]
    print(arr)
    return 

def insertion(arr):
    n = len(arr)
    for i in range(1,n):
        key = arr[i]
        j = i-1
        while j>=0 and key<arr[j]:
            arr[j+1] = arr[j]
            j-=1
        arr[j+1] = key
    print(arr)
    return 

def mergesort(arr):
    left = 0
    right = len(arr)-1
    def merge(arr,left,mid,right):
        lf = mid-left+1
        lr = right-mid
        l,r = [],[]
        for i in range(lf):
            l.append(arr[left+i])
        for i in range(lr):
            r.append(arr[mid+1+i])
        i,j,k = 0,0,left
        while i<lf and j<lr:
            if l[i]<r[j]:
                arr[k] = l[i]
                i+=1
                k+=1
            else:
                arr[k] = r[j]
                j+=1
                k+=1
        while i<lf:
            arr[k] = l[i]
            i+=1
            k+=1
        while j<lr:
            arr[k] = r[j]
            j+=1
            k+=1

    def msort(arr,left,right):
        if left>=right:
            return 
        mid = (left+right)//2
        msort(arr,left,mid)
        msort(arr,mid+1,right)
        merge(arr,left,mid,right)
    msort(arr,left,right)

def heapsort(arr):
    n = len(arr)
    def heapify(arr,i,n):
        largest = i
        left,right = 2*i+1,2*i+2
        if left<n and arr[left]>arr[largest]:
            largest = left
        if right<n and arr[right]>arr[largest]:
            largest = right
        if largest != i:
            arr[largest],arr[i] = arr[i],arr[largest]
            heapify(arr,largest,n)
    
    for i in range(n//2-1,-1,-1):
        heapify(arr,i,n)
    for i in range(n-1,0,-1):
        arr[0],arr[i] = arr[i],arr[0]
        heapify(arr,0,i)

def quicksort(arr):
    def partition(arr,low,high):
        i = low-1
        pivot = arr[high]
        for j in range(low,high):
            if arr[j]<pivot:
                i+=1
                arr[i],arr[j] = arr[j],arr[i]
        arr[i+1],arr[high] = arr[high],arr[i+1]
        return i+1
    
    def quick(arr,low,high):
        if low<high:
            pi = partition(arr,low,high)
            quick(arr,low,pi-1)
            quick(arr,pi+1,high)
    quick(arr,0,len(arr)-1)

arr = list(map(int,input().split()))
# bubble(arr)
# selection(arr)
# insertion(arr)
# mergesort(arr)
# heapsort(arr)
# quicksort(arr)
print(*arr)
