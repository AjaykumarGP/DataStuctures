

#Binary Heap

from heapq import heappush, heappop, heapify 

class MinHeap():
    def __init__(self):
        self.heap = []
    
    def parent(self, i):
        return (i-1) // 2

    #Heappush is used to insert element to last index and followed by heapify to place element at appropriate position
    def insertKey(self, k):
        heappush(self.heap, k)

    #Heappop is used to extract minimum element(heap[0]) from minHeap followed by replacing last element with removing element and heapify
    def extractMin(self):
        heappop(self.heap)

    #After replacing the desired index with negative infinity, traverse the -inf to the first position and do the heappop operation in extractmin()
    def decreaseKey(self, i, newValue):
        self.heap[i] = newValue
        while(i!=0 and self.heap[self.parent(i)] > self.heap[i]):
            self.heap[i], self.heap[self.parent(i)] = self.heap[self.parent(i)], self.heap[i]
            i = self.parent(i)


    def deleteKey(self, i):
        self.decreaseKey(i, float("-inf"))
        self.extractMin()


#Driver program to test above minHeap class
heapObj = MinHeap()
heapObj.insertKey(2)
heapObj.insertKey(3)

print(heapObj.heap)
heapObj.deleteKey(1)

heapObj.insertKey(15)
heapObj.insertKey(5)
heapObj.insertKey(4)
heapObj.insertKey(45)

print(heapObj.heap)






