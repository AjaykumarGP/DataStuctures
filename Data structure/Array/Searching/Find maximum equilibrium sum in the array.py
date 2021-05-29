






#Find maximum equilibrium sum in the array


class MaximumEquilibriumSum():
    def __init__(self, array):
        self.array = array
        self.prefixSum = []
        self.suffixSum = []
        self.totalSumSoFar = 0

    def getPrefixSum(self):
        for i in range(0, len(self.array)):
            self.totalSumSoFar += self.array[i]
            self.prefixSum.append(self.totalSumSoFar)
        self.totalSumSoFar = 0
    
    def getSuffixSum(self):
        totalSum = self.prefixSum[len(self.array)-1]
        for i in range(0, len(self.prefixSum)):
            if i == 0:
                self.suffixSum.append(totalSum)
            else:
                self.totalSumSoFar = totalSum - self.prefixSum[i-1]
            
            if self.prefixSum[i] == self.totalSumSoFar:
                print("Equlibrium sum: ", self.prefixSum[i])         
        

    def getMaximumEqulibrium(self):
        self.getPrefixSum()
        self.getSuffixSum()
        

array = [-1, 2, 3, 0, 3, 2, -1]
obj = MaximumEquilibriumSum(array)
obj.getMaximumEqulibrium()
