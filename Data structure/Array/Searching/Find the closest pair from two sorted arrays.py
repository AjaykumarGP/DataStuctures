


#Find the closest pair from two sorted arrays

class FindingClosestPair():
    def __init__(self, arrayOne, arrayTwo, key):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
        self.key = key
        self.pairList = []
        self.difference = 0
        self.lowEnd = 0
        self.highEnd = len(self.arrayTwo) - 1

    def getMinimumAbsoluteDifference(self):
        while(self.lowEnd < len(self.arrayOne) and self.highEnd > -1):

            pairSum = self.arrayOne[self.lowEnd] + self.arrayTwo[self.highEnd] 
            absoluteDifference = abs(pairSum - self.key)
            self.pairList.append([absoluteDifference, self.arrayOne[self.lowEnd], self.arrayTwo[self.highEnd]])

            if pairSum > self.key:
                self.highEnd -= 1
            elif pairSum < self.key:
                self.lowEnd += 1
            else:
                break
        self.pairList = sorted(self.pairList)
        print(self.pairList[0])

arrayOne = [1, 4, 5, 7]
arrayTwo = [10, 20, 30, 40]
key = 50
obj = FindingClosestPair(arrayOne, arrayTwo, key)
obj.getMinimumAbsoluteDifference()
