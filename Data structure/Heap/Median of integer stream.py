


from heapq import heappush, heappop, heapify



class MaxHeap():
    def __init__(self):
        self.maxHeap = []
    
    def isMaxHeapEmpty(self):
        return True if 0 == 0 else False
    
    def getMaxHeapTop(self):
        return self.maxHeap[0]
    
    def printMaxHeap(self):
        print(self.maxHeap)

    def getMaxHeapSize(self):
        return len(self.maxHeap)
    
    def maxHeappush(self, newElement):
        heappush(self.maxHeap, newElement)

    def maxHeapPop(self):
        heappop(self.maxHeap)



class MinHeap():
    def __init__(self):
        self.minHeap = []
    
    def getMinHeapTop(self):
        print("helo")
        print(self.minHeap[0])
        return self.minHeap[0]

    def getMinHeapSize(self):
        return len(self.minHeap)

    def printMinHeap(self):
        print(self.minHeap)

    def minHeapPush(self, newElement):
        heappush(self.minHeap, newElement)

    def minHeapPop(self):
        heappop(self.minHeap)
    


class MedianOfIntegerStream(MaxHeap, MinHeap):
    def __init__(self, array):
        self.dataStream = array
        self.medianList = []
        MaxHeap.__init__(self)
        MinHeap.__init__(self)

    def getMedian(self, newElement):
        if self.isMaxHeapEmpty() or self.getMaxHeapTop() > newElement:
            self.maxHeappush(newElement)
        else:
            self.minHeapPush(newElement)

        if self.getMaxHeapSize() > self.getMinHeapSize() + 1:
            self.minHeapPush(self.getMaxHeapTop())
            self.maxHeapPop()

        elif (self.getMinHeapSize() > self.getMaxHeapSize() + 1):
            self.maxHeappush(self.getMinHeapTop())
            self.minHeapPop()

        
        if self.getMaxHeapSize() == self.getMinHeapSize():
            median = (self.getMaxHeapTop() + self.getMinHeapTop()) // 2
            self.medianList.append(median)
            return
        elif(self.getMaxHeapTop() > self.getMinHeapTop()):
            self.medianList.append(self.getMaxHeapTop())
        else:
            self.medianList.append(self.getMinHeapTop())
        


    def findMedian(self):
        for i in range(0, len(self.dataStream)):
            median = self.getMedian(self.dataStream[i])
        
        self.printMinHeap()
        self.printMaxHeap()
        print(self.medianList)
            


array = [1, 2, 3, 4 ]
obj = MedianOfIntegerStream(array)
obj.findMedian()
