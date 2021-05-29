




#Find a triplet that sum to a given value
#First sort the array, then fix the first pointer by using for loop and find the second the second and third loop using two pointer technique

class FindingTriplet():
    def __init__(self, array, sum):
        self.array = array
        self.sum = sum
    
    def sortArray(self):
        self.array = sorted(self.array)
    
    def getTriplet(self):
        self.sortArray()
        for k in range(0, len(self.array)-2):
            i = k+1
            j = len(self.array)-1
            remainingSum = self.sum - self.array[k]
            while(i < j):
                sum = self.array[i] + self.array[j]
                if sum > remainingSum:
                    j -= 1
                elif sum < remainingSum:
                    i += 1
                else:
                    print("Triplet: ", self.array[k], self.array[i], self.array[j])
                    i += 1
                    j -= 1
    

array = [1, 2, 3, 4, 5]
sum = 9
obj = FindingTriplet(array, sum)
obj.getTriplet()
