


# Kth smallest element in a row-wise and column-wise sorted 2D array | Set 1


from heapq import heappush, heappop, heapify


class MinHeap():
    def __init__(self):
        self.heap = []

    def FindkSmallest(self, array, key):
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
                if len(self.resultantArray) == key:
                    print("{}rd smallest element".format(key))
                    print(self.resultantArray[key-1])
                    return
        

        while len(self.tempArray) != 0:
            heapify(self.tempArray)
            self.resultantArray.append(self.tempArray[0])
            heappop(self.tempArray)

            if len(self.resultantArray) == key:
                print("{}rd smallest element".format(key))
                print(self.resultantArray[key-1])
                return
        
        
            

         
            

array = [[2, 6, 12, 34], [1, 9, 20, 1000], [23, 34, 90, 2000]]
k = 12

heapObj = MinHeap()
heapObj.FindkSmallest(array, k)


