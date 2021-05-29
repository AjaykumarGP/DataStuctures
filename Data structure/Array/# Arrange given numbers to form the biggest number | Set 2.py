

# Arrange given numbers to form the biggest number | Set 2

import sys

def getTotalDigitOfLargestNumber(array):
    maximumValue = -sys.maxsize
    digitCount = 0
    for i in range(0, len(array)):
        if array[i] > maximumValue:
            maximumValue = array[i]

    while(maximumValue>0):
        maximumValue = maximumValue // 10
        digitCount += 1

    return digitCount


def extendArray(array, digitCount):
    extendArray = []
    for i in range(0, len(array)):
        temp = str(array[i]) * (digitCount + 1)
        extendArray.append([temp[:digitCount+1], array[i]])
    
    return extendArray

def printLargestNumber(extendedArray):
    for i in range(0, len(extendedArray)):
        print(extendedArray[i][1], end="")

def rearrange(array):
    digitCount = getTotalDigitOfLargestNumber(array)
    extendedArray = extendArray(array, digitCount)  
    extendedArray.sort(reverse=True)
    print(extendedArray)
    
    printLargestNumber(extendedArray)
      


array = [1, 34, 3, 98, 9, 76, 45, 4, 12, 121]

rearrange(array)
