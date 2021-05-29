




#Find the smallest missing number
#Using modified recursive binary search


class SmallestMissingNumber():
    def __init__(self, array):
        self.array = array
        self.missingElement = -1
        self.arraySize = len(self.array)
    
    def isFirstElementZero(self):
        if self.array[0] != 0:
            return True
        else: return False
        
    def isLastElementMissing(self):
        
        if self.array[self.arraySize-1] - self.array[0] == self.arraySize-1:
            return True
        else: return False
    
    def getArrayRange(self, start, end):
        return self.array[end] - self.array[start]
    
    def getIndexRange(self, start, end):
        return end - start
        
    def performSearch(self, low, high):

        if low < high-1:
            
            mid = (low + high) // 2
           
            if self.getArrayRange(low, mid) + 1 >  self.getIndexRange(low, mid) + 1:
                return self.performSearch(low, mid)
            else:
                return self.performSearch(mid, high)
                
        else:

            if self.getArrayRange(low, high) != 1:
                return self.array[low]
            else:
                return self.array[high]
            
            

    def getMissingNumber(self):
        if self.isFirstElementZero():
            self.missingElement = 0 
        elif self.isLastElementMissing():
            self.missingElement = self.array[self.arraySize-1] + 1
        else:
            #Perform modified binary search
            print("Binary search activated")
            self.missingElement = self.performSearch(0, self.arraySize-1) + 1
            
        print(self.missingElement)


array = [ 0, 1, 2, 3, 4, 5, 6, 7, 10 ]
obj = SmallestMissingNumber(array)
obj.getMissingNumber()
