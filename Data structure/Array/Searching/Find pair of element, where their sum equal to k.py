

#Find pair of element, where their sum equal to k
#Two pointer approach

class SumOfPairOperation():
    def __init__(self, array, key):
        self.array = array
        self.key = key
        self.pair = []
    
    def sortArray(self):
        self.array = sorted(self.array)
    
    def findPair(self):
        self.sortArray()
        firstPointer = 0
        secondPointer = len(self.array) - 1

        while(firstPointer < secondPointer):
            if self.array[firstPointer] + self.array[secondPointer] > self.key:
                secondPointer -= 1
            elif self.array[firstPointer] + self.array[secondPointer] < self.key:
                firstPointer += 1
            else:
                self.pair.append([self.firstPointer], self.array[secondPointer])
                break

        print(self.pair)

array = [1, 4, 45, 6, 10, 8]
k = 16

obj = SumOfPairOperation(array, k)
obj.findPair()
