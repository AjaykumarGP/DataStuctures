





#Finding the leader in the array element

class FindingLeader():
    def __init__(self, array):
        self.array = array
    
    def findLeader(self):
        for i in range(len(self.array)-1, -1, -1):
            if i == len(self.array)-1:
                print(self.array[i])

            if i > 0 and self.array[i] > self.array[i-1]:
                print(self.array[i])
            

array = [16, 17, 4, 3, 5, 2]
obj = FindingLeader(array)
obj.findLeader()
