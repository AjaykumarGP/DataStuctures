




def rotateArray(array, rotationKey, index):
    for i in range(len(rotationKey)-1, -1, -1): #Important - Reversal is the key
        leftBound = rotationKey[i][0]
        rightBound = rotationKey[i][1]
        if index >= leftBound and index <= rightBound:#Check whether the index is within the boundary
            if index == leftBound: #Check is whether the index is equal to leftBound
                index = rightBound
            else:
                index = index - 1 #Else the index will be within boundary

    print(array[index])



array = [1,2,3,4,5]
rotationKey= [[0,2], [0,3]]
index = 1
rotateArray(array, rotationKey, index)




