


#Rearrange array such that arr[i] >= arr[j] if i is even and arr[i]<=arr[j] if i is odd and j < i

#Method

#1. Sorted using quicksort
#2. Reversed recursive algorithm

def dividePartition(array, low, high):
    
    pivotIndex = high
    traversePointer = low

    for i in range(low, high+1):
        if(array[traversePointer] > array[pivotIndex]):
            temp = array[traversePointer]
            array[traversePointer] = array[pivotIndex-1]
            array[pivotIndex-1] = array[pivotIndex]
            array[pivotIndex] = temp
            pivotIndex -= 1
        else:
            traversePointer += 1

    return pivotIndex 


def quickSort(array, low, high):
    if(low<high):
        partition = dividePartition(array, low, high)
        quickSort(array, low, partition-1)
        quickSort(array, partition+1, high)
    return array    
    
def rearrangeSortedArray(array, start, end):

        if(start < end):
            rearrangeSortedArray(array, start+1, end-1)
            print(array[start], array[end], end=" ")
            return
        else:
            return
    



array = [1, 2, 1, 4, 5, 6, 8, 8]
sortedArray = quickSort(array, 0, len(array)-1)


if len(array) % 2 == 0:
    rearrangeSortedArray(sortedArray, 0, len(array)-1)
else:
    rearrangeSortedArray(sortedArray[1:], 0, len(array[1:])-1)
    print(array[0])
    














