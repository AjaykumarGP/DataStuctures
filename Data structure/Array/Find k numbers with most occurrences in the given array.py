
from heapq import heappush, heappop, heapify
import heapq

# Find k numbers with most occurrences in the given array

class MaxHeap():
    def __init__(self):
        self.maxHeap = []
    
    def heapify(self):
        return heapq._heapify_max(self.maxHeap)

class KMostOccurance(MaxHeap):
    def __init__(self, array, key):
        self.frequencyDict = {}
        self.array = array
        self.key = key
        MaxHeap.__init__(self)

    def createHashMap(self):
        for i in range(0, len(self.array)):
            if self.array[i] in self.frequencyDict:
                self.frequencyDict[self.array[i]] += 1
            else:
                self.frequencyDict[self.array[i]] = 1
    
    def createPriorityQueue(self):
        for i in self.frequencyDict:
            self.maxHeap.append((self.frequencyDict[i], i))
        self.heapify()
    
    def printKMaximumFrequency(self):
        for i in range(self.key):
            print(self.maxHeap[0][1])
            heapq._heappop_max(self.maxHeap)
            


array = [7, 10, 11, 5, 2, 5, 5, 7, 11, 8, 9]
key = 4
obj = KMostOccurance(array, key)
obj.createHashMap()
obj.createPriorityQueue()
obj.printKMaximumFrequency()

