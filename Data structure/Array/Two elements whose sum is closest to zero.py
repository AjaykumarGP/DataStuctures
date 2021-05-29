


# Two elements whose sum is closest to zero

import sys

class PairClosestToZero():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)

    def sortArray(self):
        self.array = sorted(self.array)
    
    def findSumOfPair(self, pointerOne, pointerTwo):
        return self.array[pointerOne] + self.array[pointerTwo]

    def findNumberPair(self):
        leftPointer = 0
        rightPointer = len(self.array)-1
        numberClosestToZero = sys.maxsize
        pairOne = 0
        pairTwo = 0

        self.sortArray()

        while(leftPointer < rightPointer):
            
            pairSum = self.findSumOfPair(leftPointer, rightPointer)
            if pairSum > 0:
                if abs(pairSum) < numberClosestToZero:
                    numberClosestToZero = pairSum
                    pairOne = self.array[leftPointer]
                    pairTwo = self.array[rightPointer]
                rightPointer -= 1
            else:
                if abs(pairSum) < numberClosestToZero:
                    numberClosestToZero = pairSum
                    pairOne = self.array[leftPointer]
                    pairTwo = self.array[rightPointer]
                leftPointer += 1
                
        print(numberClosestToZero)
        print(pairOne)
        print(pairTwo)




array = [1, 60, -10, 70, -80, 85]
obj = PairClosestToZero(array)
obj.findNumberPair()
