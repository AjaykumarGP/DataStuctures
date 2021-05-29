




# Find a triplet such that sum of two equals to third element
#First sort the array, then fix the first pointer by using for loop(Traverse from backward) and find the second the second and third loop using two pointer technique

class FindingTriplet():
    def __init__(self, array, sum):
        self.array = array
        self.sum = sum
    
    def sortArray(self):
        self.array = sorted(self.array)
    
    def getTriplet(self):
        self.sortArray()
        for k in range(len(self.array)-1, -1, -1):
            i = k - 1
            j = 0
            while(j < i):
                if self.array[i] + self.array[j] < self.array[k]:
                    j += 1
                elif self.array[i] + self.array[j] > self.array[k]:
                    i -= 1
                else:
                    print("Triplets: ", self.array[k], self.array[j], self.array[i])
                    i -= 1
                    j += 1
    

array = [5, 32, 1, 7, 10, 50, 19, 21, 0]
sum = 0
obj = FindingTriplet(array, sum)
obj.getTriplet()
