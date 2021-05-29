





from heapq import heappush, heappop, heapify
import heapq


class MaxHeap():
    def __init__(self):
        self.maxHeap = []

    def heapify(self):
        return heapq._heapify_max(self.maxHeap)
    
    def getMaxHeapTop(self):
        return self.maxHeap[0]



class MaximumSumCombination(MaxHeap):
    def __init__(self, arrayOne, arrayTwo):
        MaxHeap.__init__(self)
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
    
    def getArrayOneMax(self):
        return max(self.arrayOne)

    def getArrayTwoMax(self):
        return max(self.arrayTwo)

    def findSum(self, arrayOne, arrayTwo):
        
        for i in range(len(arrayTwo)-1, -1, -1):
            for j in range(0, len(arrayOne)):
                self.maxHeap.append((arrayOne[j] + arrayTwo[i]))             
        self.heapify()

    def sortArray(self, array):
        return sorted(array)

    def getKMaximumSum(self, key):
        
        for i in range(0, key):
            print(self.maxHeap[0])
            heapq._heappop_max(self.maxHeap)
            
        
    def findKMaximumSum(self, key):
    
        if self.getArrayTwoMax() > self.getArrayOneMax():
            self.findSum(self.arrayOne, self.sortArray(self.arrayTwo))
        else: 
            self.findSum(self.sortArray(self.arrayTwo), self.arrayOne)
            
        
        self.getKMaximumSum(key)
        
        
            

arrayOne = [3, 2]
arrayTwo = [1, 4]
key = 2

classObj = MaximumSumCombination(arrayOne, arrayTwo)
classObj.findKMaximumSum(key)
