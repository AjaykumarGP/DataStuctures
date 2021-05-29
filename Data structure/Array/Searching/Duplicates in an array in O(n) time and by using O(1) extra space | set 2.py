


#Duplicates in an array in O(n) time and by using O(1) extra space
#Input range = 0 to n-1
#Three method: 1. Negation value method, but will only work not more than two repetitive element in the array
                # T.C: O(n) and S.P: O(1)
            #2. External Hashmap approach T.C: O(N) and S.P: O(N)
            #3. Internal hashmap method within the array using "%" and "/" O(n) and O(1)

# 2. External Hashmap approach T.C: O(N) and S.P: O(N)
class FindingDuplicate():
    def __init__(self, array):
        self.array = array
        self.hashmap = {}
    
    def getDuplicateElement(self):
        for i in range(0, len(self.array)):
            if self.array[i] in self.hashmap.keys():
                print("Duplicate element: ", self.array[i])
            else:
                self.hashmap[self.array[i]] = 1

array = [2,7,1,4,1,7,8,2,8]
obj = FindingDuplicate(array)
obj.getDuplicateElement()
