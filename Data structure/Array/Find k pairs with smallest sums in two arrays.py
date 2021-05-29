



#Find k pairs with smallest sums in two arrays
#Difficulty - Hard :)

from heapq import heapify, heappush, heappop

class MinHeap():
    def __init__(self, heapSize):
        self.minHeap = []
        self.heapSize = heapSize
        self.auxiliaryArray = []
    
    def extractKPairs(self):
        if len(self.minHeap) != self.heapSize:
            return -1
        else:
            self.auxiliaryArray.append(self.minHeap[0])
            heappop(self.minHeap)
            self.heapify()

            if len(self.auxiliaryArray) == self.heapSize:
                return 1
            else: 
                return -1

    def findKSmallestSum(self, value):
        self.minHeap.append(value)
        self.heapify()
        return self.extractKPairs()
    
    def heapify(self):
        return heapify(self.minHeap)
    
    

class SmallestSumPairsOperation(MinHeap):
    def __init__(self, arrayOne, arrayTwo, key):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
        self.key = key
        MinHeap.__init__(self, key)
        

    def getSmallestSumPair(self, arrayOne, arrayTwo):
        KeyCounter = 0
        result = -1
        
        for i in range(0,len(self.arrayOne)):
            for j in range(0, len(self.arrayTwo)):
                result = self.findKSmallestSum((self.arrayOne[i] + self.arrayTwo[j], self.arrayOne[i], self.arrayTwo[j]))
                
                if result == 1:
                    break
            if result == 1:
                break
     
        print(self.auxiliaryArray)
                

    def getSmallestSum(self):
        
        if self.arrayOne[0] < self.arrayTwo[0]:
            self.getSmallestSumPair(arrayOne, arrayTwo)
        else:
            self.getSmallestSumPair(arrayTwo, arrayOne)



arrayOne = [1, 7, 11]
arrayTwo = [2, 4, 6]
key = 3

obj = SmallestSumPairsOperation(arrayOne, arrayTwo, key)
obj.getSmallestSum()
