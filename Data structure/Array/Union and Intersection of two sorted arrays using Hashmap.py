





#Union and Intersection of two sorted arrays using hashmap


class UnionAndIntersection():
    def __init__(self, arrayOne, arrayTwo):
        self.arrayOne = arrayOne
        self.arrayTwo = arrayTwo
        self.dict = {}
        self.union = []
        self.intersection = []

    def getUnionAndIntersection(self):
        arrayOneSize = len(self.arrayOne)
        arrayTwoSize = len(self.arrayTwo)

        i = j = 0
        while(i < arrayOneSize or j < arrayTwoSize):
            if (i < arrayOneSize):
                if self.arrayOne[i] in self.dict.keys():
                    if self.arrayOne[i-1] != self.arrayOne[i]:
                        self.intersection.append(self.arrayOne[i])
                    else:
                        self.union.append(self.arrayOne[i])
                else:
                    self.dict[self.arrayOne[i]] = 1
                    self.union.append(self.arrayOne[i])
                
            
            if (j<arrayTwoSize):
                if self.arrayTwo[i] in self.dict.keys():
                    self.intersection.append(self.arrayTwo[i])
                else:
                    self.dict[self.arrayTwo[i]] = 1
                    self.union.append(self.arrayTwo[i])
            i += 1
            j += 1
        print(self.intersection)
        print(self.union)

            



arrayOne = [2, 5, 6, 6]
arrayTwo = [4, 6, 8, 10]
obj = UnionAndIntersection(arrayOne, arrayTwo)
obj.getUnionAndIntersection()
