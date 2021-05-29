



# Minimum number of swaps required to sort an array

class MinimumSwap():
    def __init__(self, array):
        self.originalArray = array
        self.sortedArray = []
        self.minimumSwap = 0
        self.indexDict = {}
    
    def copyAndSort(self):
        self.sortedArray = self.originalArray.copy()
        self.sortedArray = sorted(self.sortedArray)

    def getIndexCount(self):
        for i in range(0, len(self.originalArray)):
            self.indexDict[self.originalArray[i]] = i
    
    def getSwapIndex(self, swapElement):
        return self.indexDict[swapElement]

    def performSwapOperation(self):
        for i in range(0, len(self.originalArray)):
            if self.originalArray[i] != self.sortedArray[i]:
                index = self.getSwapIndex(self.sortedArray[i])

                #Update the index in hashmap too
                self.indexDict[self.originalArray[i]] = index
                self.indexDict[self.originalArray[index]] = i

                self.originalArray[i], self.originalArray[index] = self.originalArray[index], self.originalArray[i]
                self.minimumSwap += 1
        
    def getMinimumSwap(self):
        self.copyAndSort()
        self.getIndexCount()
        self.performSwapOperation()
    
    def printMinimumSwap(self):
        print("Minimum number of swaps required is",self.minimumSwap)

    
array = [1, 5, 4, 3, 2]
obj = MinimumSwap(array)
obj.getMinimumSwap()
obj.printMinimumSwap()
