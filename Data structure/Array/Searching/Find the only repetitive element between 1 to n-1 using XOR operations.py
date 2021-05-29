




#Find the only repetitive element between 1 to n-1
# XOR operations

class FindingRepetitiveNUmber():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)
        self.result = 0

    def getRepetitiveNumber(self):
        
        #XOR all the elements in original array
        for i in range(0, self.arraySize):
            self.result ^= self.array[i]

        #And XOR all the number from 1 to n-1
        for j in range(1, self.arraySize):
            self.result ^= j

    def printRepetitiveNumber(self):
        print(self.result)


array = [1, 5, 1, 2, 3, 4]
obj = FindingRepetitiveNUmber(array)
obj.getRepetitiveNumber()
obj.printRepetitiveNumber()
