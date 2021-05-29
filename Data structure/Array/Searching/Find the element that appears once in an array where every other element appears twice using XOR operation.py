




# Find the element that appears once in an array where every other element appears twice

class FindingRepetitiveNUmber():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)
        self.result = 0

    def getRepetitiveNumber(self):
        
        #XOR all the elements in original array
        for i in range(0, self.arraySize):
            self.result ^= self.array[i]

    def printRepetitiveNumber(self):
        print(self.result)


array = [7, 3, 5, 4, 5, 3, 4]
obj = FindingRepetitiveNUmber(array)
obj.getRepetitiveNumber()
obj.printRepetitiveNumber()
