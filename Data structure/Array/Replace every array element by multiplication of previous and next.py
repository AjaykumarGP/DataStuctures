


#Replace every array element by multiplication of previous and next


def rearrange(array):
    previousElement = 0
    arraySize = len(array)
    for i in range(0, len(array)):
        if i == 0:
            previousElement = array[i]
            array[i] = previousElement * array[i+1]
        elif(i==len(array)-1):
            array[arraySize-1] = previousElement * array[arraySize-1]
        else:
            temp = array[i]
            array[i] = previousElement * array[i+1]
            previousElement = temp
    print(array)
            

array = [2, 3, 4, 5, 6]

rearrange(array)
