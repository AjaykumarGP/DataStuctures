




# Rearrange an array in maximum minimum form | Set 2 (O(1) extra space)

def rearrange(array):
    arraySize = len(array)
    minElement = 0
    maxElement = arraySize-1

    for i in range(0, len(array)):
        
        if i%2 == 0: #Odd position
            array[i] = array[i] + ((array[maxElement] % (arraySize+1)) * (arraySize+1))
            maxElement -= 1
        else:        #Even position
            array[i] = array[i] + ((array[minElement] % (arraySize+1)) * (arraySize+1))
            minElement += 1
        
        print(array)

    for i in range(0, len(array)):
        print(array[i]//(arraySize+1), end=" ")



array = [1, 2, 3, 4, 5, 6, 7]
rearrange(array)

