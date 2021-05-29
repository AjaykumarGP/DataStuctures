


import sys

# Find Second largest element in an array

class SecondLargestElement():
    def __init__(self, array):
        self.array = array
    
    def findSecondLargest(self):

        self.first = -sys.maxsize
        self.second = -sys.maxsize
        for i in range(0, len(self.array)):
            if self.array[i] >= self.first:
                self.second = self.first
                self.first = self.array[i]

            elif self.array[i] > self.second and self.array[i] < self.first:
                self.second = self.array[i]

    def printSecondLargest(self):
        print(self.second)
        
array = [5, 35, 1, 10, 2, 1]
obj = SecondLargestElement(array)
obj.findSecondLargest()
obj.printSecondLargest()

