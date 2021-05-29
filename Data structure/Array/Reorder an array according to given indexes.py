

#Reorder an array according to given indexes

def rearrange(array, indexArray):
    indexCounter = 0

    while(indexCounter < len(array)):
        if indexArray[indexCounter] != indexCounter:
            array[indexArray[indexCounter]], array[indexCounter] = array[indexCounter], array[indexArray[indexCounter]]
            indexArray[indexArray[indexCounter]], indexArray[indexCounter] =  indexArray[indexCounter], indexArray[indexArray[indexCounter]]
        else:
            indexCounter += 1

    print(array)


array = [10, 11, 12]
indexArray = [1,0,2]

rearrange(array, indexArray)

#Time complexity = O(n)
#Space complexity = O(1)
