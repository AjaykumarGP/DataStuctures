

#Maximum Subarray Sum Excluding Certain Elements
# Modified Kadane's algorithm and hashmap

class MaximumSubArraySum():
    def __init__(self, arrayOne, arrayTwo):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
        self.maximumSubarraySumList = []
        self.maximumSum = 0
        self.hashmap = {}
    
    def createHashmap(self):
        for i in range(0, len(self.arrayTwo)):
            self.hashmap[self.arrayTwo[i]] = 1

    def performKadaneAlgorithm(self):
        for i in range(0, len(self.arrayOne)):
            if self.arrayOne[i] not in self.hashmap.keys():
                self.maximumSum += self.arrayOne[i]
            else:
                self.maximumSubarraySumList.append(self.maximumSum)
                self.maximumSum = 0
            
            if i == len(self.arrayOne)-1:
                self.maximumSubarraySumList.append(self.maximumSum)
                self.maximumSum = 0

    def printMaximumSubarraySum(self):
        print(max(self.maximumSubarraySumList))

    def getMaximumSubarray(self):
        self.createHashmap()
        self.performKadaneAlgorithm()
        self.printMaximumSubarraySum()
        
    
arrayOne = [3, 4, 5, -4, 6]
arrayTwo = [1, 8, 5]

obj = MaximumSubArraySum(arrayOne, arrayTwo)
obj.getMaximumSubarray()
