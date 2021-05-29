





#Union and Intersection


class UnionAndIntersection():
    def __init__(self, arrayOne, arrayTwo):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
        self.dict = {}
        self.union = []
        self.intersection = []

    def findUnion(self):
        arrayOneSize = len(self.arrayOne) - 1
        arrayTwoSize = len(self.arrayTwo) - 1

        i = j = 0
        while(i <= arrayOneSize and j <= arrayTwoSize):
            
            while(i < arrayOneSize and self.arrayOne[i] == self.arrayOne[i+1]):
                i += 1

            while(j < arrayTwoSize and self.arrayTwo[j] == self.arrayTwo[j+1]):
                j += 1
            
            if self.arrayOne[i] < self.arrayTwo[j]:
                self.union.append(self.arrayOne[i])
                i += 1
            elif self.arrayOne[i] > self.arrayTwo[j]:
                self.union.append(self.arrayTwo[j])
                j += 1
            else:
                self.union.append(self.arrayOne[i])
                i += 1
                j += 1
        
        while(i <= arrayOneSize):
            while(i < arrayTwoSize and self.arrayOne[i] == self.arrayOne[i+1]):
                i += 1
            self.union.append(self.arrayOne[i])
            i += 1
        
        while(j <= arrayTwoSize):
            
            while(j < arrayTwoSize and self.arrayTwo[j] == self.arrayTwo[j+1]):    
                j += 1
            
            self.union.append(self.arrayTwo[j])
            j += 1
        
        print(self.union)

    def findIntersection(self):

        arrayOneSize = len(self.arrayOne) - 1
        arrayTwoSize = len(self.arrayTwo) - 1

        i = j = 0
        while(i <= arrayOneSize and j <= arrayTwoSize):
            
            while(i < arrayOneSize and self.arrayOne[i] == self.arrayOne[i+1]):
                i += 1

            while(j < arrayTwoSize and self.arrayTwo[j] == self.arrayTwo[j+1]):
                j += 1
            
            if self.arrayOne[i] < self.arrayTwo[j]:
                i += 1
            elif self.arrayOne[i] > self.arrayTwo[j]:
                j += 1
            else:
                self.intersection.append(self.arrayOne[i])
                i += 1
                j += 1
        
        
        
        print(self.intersection)
        

            



arrayOne = [1, 2, 2, 2, 3]
arrayTwo = [2, 3, 4, 5]
obj = UnionAndIntersection(arrayOne, arrayTwo)
obj.findUnion()
obj.findIntersection()
