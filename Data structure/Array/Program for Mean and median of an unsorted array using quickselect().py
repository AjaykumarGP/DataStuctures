

import random


#Program for Mean and median of an unsorted array using quickselect()

class MedianExtractor():
    
    def __init__(self):
        self.array = []

    def shufflePivotIndex(self, low, high):
        if low<high:
            pivot = random.randrange(low, high)
            self.array[pivot], self.array[high] = self.array[high], self.array[pivot]
            return

    def lomutoPartition(self, low, high):

        self.shufflePivotIndex(low, high)
        pivotIndex = high       
        trackingIndex = low

        for i in range(low, high+1):
            if self.array[trackingIndex] > self.array[pivotIndex]:
                temp = self.array[trackingIndex]
                self.array[trackingIndex] = self.array[pivotIndex-1]
                self.array[pivotIndex-1] = self.array[pivotIndex]
                self.array[pivotIndex] = temp
                pivotIndex -=1

            else:trackingIndex += 1
        

        return pivotIndex



    def quickselect(self, low, high, medianIndex):
        if low<=high:
            mid = self.lomutoPartition(low, high)
            print(mid, medianIndex)
            
            if mid == medianIndex:
                return self.array[mid]
            
            if mid > medianIndex:
                return self.quickselect(low, mid-1, medianIndex)
            
            elif mid < medianIndex:
                return self.quickselect(mid+1, high, medianIndex)

    def getMedian(self, array):
        return (len(array) + 1) // 2

    def copyArray(self, array):
        self.array = array.copy()
        
            

    
array = [1, 3, 5, 2, 6, 6, 8, 7, 9, 10, 11, 13, 14, 15, 16]

heapObj = MedianExtractor()
medianIndex = heapObj.getMedian(array)
heapObj.copyArray(array)
print("median index", medianIndex)
median = heapObj.quickselect( 0, len(array)-1, medianIndex-1)
print("Median of the given array")
print(median)
