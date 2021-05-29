


# K’th Smallest/Largest Element in Unsorted Array | Set 1

def partition(array, low, high, k):

    
    pivotIndex = high
    monitorIndex = low

    
    for i in range(low, high+1):
        if(array[monitorIndex] > array[pivotIndex]):
            temp = array[monitorIndex]
            array[monitorIndex] = array[pivotIndex-1]
            array[pivotIndex-1] = array[pivotIndex]
            array[pivotIndex] = temp
            pivotIndex -= 1
        else:
            monitorIndex += 1
    

    return pivotIndex

def findSmallestElement(array, low, high, k):
    if(low<=high):

        mid = partition(array, low, high, k)
        
        if mid+1 == k:
            
            return(array[mid])
        if k < mid+1:
            
            return findSmallestElement(array, low, mid-1, k)
        else:
            
            return findSmallestElement(array, mid+1, high, k)


array = [7, 10, 4, 3, 20, 15]
k = 6

kthElement = findSmallestElement(array, 0, len(array)-1, k)
print(kthElement)



