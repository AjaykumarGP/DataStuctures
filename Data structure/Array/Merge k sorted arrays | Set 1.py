


#Merge k sorted arrays | Set 1

from heapq import heappush, heappop, heapify


class MinHeap():
    def __init__(self):
        self.heap = []

    def mergeSortedArray(self, array, key):
        self.tempArray = []
        self.resultantArray = []

        index = 0
        indexTwo = 0

        for i in range(0, len(array[0])): #Inner list
            for j in range(0, len(array)): #Outer list

                self.tempArray.append(array[j][i])

                if len(self.tempArray) == key:    
                    #Perform Minheap on tempArray and extract minimum element
                    heapify(self.tempArray)
                    self.resultantArray.append(self.tempArray[0])
                    heappop(self.tempArray)
        

        while len(self.tempArray) != 0:
            heapify(self.tempArray)
            self.resultantArray.append(self.tempArray[0])
            heappop(self.tempArray)
        print(self.resultantArray)
            

         
            

array = [[2, 6, 12, 34], [1, 9, 20, 1000], [23, 34, 90, 2000]]
key = 3

heapObj = MinHeap()
heapObj.mergeSortedArray(array, key)


