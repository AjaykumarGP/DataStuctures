


#Duplicates in an array in O(n) time and by using O(1) extra space
#Input range = 0 to n-1
#Three method: 1. Negation value method, but will only work not more than two repetitive element in the array
                # T.C: O(n) and S.P: O(1)
            #2. External Hashmap approach T.C: O(N) and S.P: O(N)
            #3. Internal hashmap method within the array using "%" and "/" O(n) and O(1)

#Internal hashmap method within the array using "%" and "/" O(n) and O(1)
#Order maintained
class FindingDuplicate():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)
    
    def getDuplicateElement(self):
        for i in range(0, len(self.array)):
            index = self.array[i] % self.arraySize
            self.array[index] += self.arraySize
            if self.array[index] // self.arraySize > 1 and self.array[index] // self.arraySize <= 2:
                print("Duplicate elements: ", index)
        
        
array = [6, 3, 3, 4, 5, 6, 6, 6,  4]
obj = FindingDuplicate(array)
obj.getDuplicateElement()
