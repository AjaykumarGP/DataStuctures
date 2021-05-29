

#Heap sort

from heapq import heappush, heappop, heapify 


class HeapSort(): #Max heap
    def __init__(self):
        self.heap = []
    
    def maxHeapify(self, n, i):
        
        greatestElement = i

        leftNode = (2 * i) + 1
        rightNode = (2 * i) + 2

        if leftNode < n and self.heap[greatestElement] > self.heap[leftNode]:
            greatestElement = leftNode

        if rightNode < n and self.heap[greatestElement] > self.heap[rightNode]:
            greatestElement = rightNode 

        if greatestElement != i:
            self.heap[i], self.heap[greatestElement] = self.heap[greatestElement], self.heap[i]
            self.maxHeapify(n, greatestElement)       

    
    def insertKey(self, key):
        heappush(self.heap, key)
        

    def heapSort(self):
        for i in range(len(self.heap)-1, 0, -1):
            self.heap[i], self.heap[0] = self.heap[0], self.heap[i]
            self.maxHeapify(i, 0)
            
    
    def printHeap(self):
        print(self.heap)

    

array = [12, 11, 13, 5, 6, 7]

heapObj = HeapSort()

#Build a heap with heapifying every element, O(n)
for i in range(0, len(array)):
    heapObj.insertKey(array[i])

heapObj.heapSort()
heapObj.printHeap()

