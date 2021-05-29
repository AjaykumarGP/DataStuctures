






# k smallest elements in same order using O(1) extra space
#To find K smallest/greatest elements in an unsorted array, use insertion sort method, because it is stable sorting algorithm

class ModifiedInsertionSort():
    def __init__(self, array, key):
        self.array = array
        self.key = key
    
    def getMaximum(self):
        return max(self.array[:self.key])

    def getKMaximumStableElement(self):
        #Modified insertion sort
        for i in range(key, len(self.array)):
            flag = False
            maxElement = self.getMaximum()
            if self.array[i] < maxElement:
                j=0
                while(j <= key-1):
                    if self.array[j] == maxElement or flag == True:
                        flag = True
                        self.array[j] = self.array[j+1]
                    j += 1
                self.array[key-1] = self.array[i]
                self.array[i] = maxElement 
            print(self.array) 
            


array = [7,2,8,1,3,0,9]
key = 3
obj = ModifiedInsertionSort(array, key)
obj.getKMaximumStableElement()
