
#Minimum product of k integers in an array of positive Integers

from heapq import heappush, heappop, heapify


class MinHeapOperation():
    def __init__(self, array):
        self.minHeap = array
        self.minimumProduct = 1
        heapify(self.minHeap)

    def getMinimumProduct(self, key):
        for i in range(0, key):
            self.minimumProduct *= heappop(self.minHeap)
        print(self.minimumProduct) 



array = [198, 76, 544, 123, 154, 675]
key = 2
obj = MinHeapOperation(array)
obj.getMinimumProduct(key)
    
    

