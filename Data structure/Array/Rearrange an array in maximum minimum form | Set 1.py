

# Rearrange an array in maximum minimum form | Set 1

def reverseArray(array, start, end):
    tempArray = [0 for i in range(0, len(array))]
    index = 0
    while(start <= end):
        
        if start == end:
            tempArray[index] = array[start]
            return tempArray
        
        tempArray[index] = array[end]
        index += 1
        tempArray[index] = array[start]
        index += 1

        start += 1
        end -= 1
    return tempArray

def copyAuxiliaryArrayToOriginalArray(modifiedArray, array):
    for i in range(0, len(array)):
        array[i] = modifiedArray[i]
    return array

def rearrangeArray(array):
    newArray = reverseArray(array, 0, len(array)-1)
    array = copyAuxiliaryArrayToOriginalArray(newArray, array)
    print(array)

array = [1, 2, 3, 4, 5, 6]
rearrangeArray(array)
