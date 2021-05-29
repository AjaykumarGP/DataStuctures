


# Find the Rotation Count in Rotated Sorted array

def getPivotIndex(array):
    for i in range(0, len(array)):
        if(array[i] > array[(i+1)%len(array)]):
            return i+1

def countRotation(array):
    pivotIndex = getPivotIndex(array)
    return pivotIndex

def getPivotIndexBinarySearch(array, low, high):

    #Edge case
    #check if the array is fully sorted
    if(array[low] < array[high]):
        return low
    
    if(high==low):
        return low

    mid = (low + high) // 2

    if(array[mid] > array[mid+1]):
        return mid
    elif(array[mid] < array[mid-1]):
        return mid-1
    
    if array[high] < array[mid]:
        return getPivotIndexBinarySearch(array, mid+1, high)
    else:
        return getPivotIndexBinarySearch(array, low, mid-1) 

def printResult(array, key):
    #Linear search
    # print(countRotation(array))

    #BinarySearch
    print(getPivotIndexBinarySearch(array, 0, len(array)-1) + 1)

array = [2, 3, 6, 12]
key = 7

printResult(array, key)

