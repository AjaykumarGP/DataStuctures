


#Search an element in a sorted and rotated array

def binarySearch(array, start, end, key):
    if(start>end):
        return -1

    mid = (start + end) // 2
    
    
    if(array[mid] == key):
        return mid

    if(array[start] <= array[mid]): #check if the partial array is sorted
        if(key>=array[start] and key<=array[mid]):
            return binarySearch(array, start, mid-1, key)
        else:
            return binarySearch(array, mid+1, end, key)
    else:
        if(key>=array[mid] and key<=array[end]):
            return binarySearch(array, mid+1, end, key)
        else:
            return binarySearch(array, start, mid-1, key)

   

def printResult(array, key):
    if(binarySearch(array, 0, len(array)-1, key) != -1):
        print("KeyFound")
    else:
        print("keyNotFound")

array = [3,4,5,6,7,1,2]
key = 7

printResult(array, key)

