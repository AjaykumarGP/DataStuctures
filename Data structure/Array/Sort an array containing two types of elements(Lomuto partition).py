








#Sort an array containing two types of elements

class LomutoPartitionAlgorithm():
    def __init__(self, array):
        self.array = array
    
    def sortRandomArray(self):
        firstPointer = 0
        secondPointer = len(self.array)-1

        while(firstPointer < secondPointer):
            if self.array[firstPointer] == 0:
                firstPointer += 1
            else:
                if self.array[secondPointer] == 0:
                    self.array[firstPointer], self.array[secondPointer] = self.array[secondPointer], self.array[firstPointer]
                    firstPointer += 1
                    secondPointer -= 1
                else:
                    secondPointer -= 1

        print(self.array)




array = [1, 1, 1, 0, 1, 0, 0, 1, 1, 1, 1]
obj = LomutoPartitionAlgorithm(array)
obj.sortRandomArray()
