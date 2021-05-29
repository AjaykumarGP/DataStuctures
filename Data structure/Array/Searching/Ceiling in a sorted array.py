



#Ceiling in the sorted array

class FindingCeiling():
    def __init__(self, array, x):
        self.array = array
        self.x = x

    def findFloorandCeiling(self, low, high):
        if low < high:
            mid = (low + high) // 2
            if self.array[mid] == self.x:
                
                print(self.array[mid])
                return mid
            if self.array[mid] > self.x:
                return self.findFloorandCeiling(low, mid-1)
            else:
                return self.findFloorandCeiling(mid + 1, high)
        print(low, high)
        if self.array[low] > self.x and low > 0 and low < len(self.array):
            print("Ceiling: ", self.array[low])
            print("Floor: ", self.array[low-1])
        elif(self.array[low] < self.x and low > 0 and low < len(self.array)):
            print("Ceiling: ", self.array[low])
            print("Floor: ", self.array[low+1])
        elif(low == 0):
            print("Ceiling: ", self.array[low])
            print("Floor: ", "No floor exist")
        else:
            print("Ceiling: ", "No ceiling exist")
            print("Floor: ", self.array[low])
        
        


    def getFloorAndCeiling(self):
        self.findFloorandCeiling(0, len(self.array))


array = [1, 2, 8, 10, 10, 12, 19]
x = 1
obj = FindingCeiling(array, x)
obj.getFloorAndCeiling()

