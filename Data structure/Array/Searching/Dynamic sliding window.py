






# Find subarray with given sum | Set 1 (Nonnegative Numbers)
#Dynamic sliding window

class DynamicSlidingWindow():
    def __init__(self, array, sum):
        self.array = array
        self.arraySize = len(array)
        self.sum = sum

    def getSubarray(self):
        leftPointer = 0
        rightPoint = 1
        maximumSum = 0
        currentWindowSum = self.array[leftPointer]

        while(rightPoint < self.arraySize):
            currentWindowSum += self.array[rightPoint]
            rightPoint += 1
            if currentWindowSum > self.sum:
                currentWindowSum -= self.array[leftPointer]
                leftPointer += 1
            elif currentWindowSum == self.sum:
                print(currentWindowSum)
                print("Sub array index: ", leftPointer, rightPoint-1)
                return
            

        print("No subarray found")


array = [15, 2, 4, 8, 9, 5, 10, 23]
sum = 23
obj = DynamicSlidingWindow(array, sum)
obj.getSubarray()
