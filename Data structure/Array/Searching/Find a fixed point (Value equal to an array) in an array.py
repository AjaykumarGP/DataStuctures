




# Find a Fixed Point (Value equal to index) in a given array

class FindingFixedPoint():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)

    def binarySearch(self, low, high):
        if low<high:
            mid = (low + high) // 2
            
            if self.array[mid] == mid:
                print("Fixed point: ", self.array[mid])
                return
            elif self.array[mid] > mid:
                self.binarySearch(low, mid-1)
            elif self.array[mid] < mid:
                self.binarySearch(mid+1, high)

    def getFixedPoint(self):
        self.binarySearch(0, self.arraySize-1)


array = [0, 1, 2, 8, 17]
obj = FindingFixedPoint(array)
obj.getFixedPoint()
