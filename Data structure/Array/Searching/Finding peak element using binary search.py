







# Find peak element

class FindingPeakElement():
    def __init__(self, array):
        self.array = array

    def peakBinarySearch(self, low, high):
        if low < high:
            mid = (low + high) // 2

            if mid == 0:
                if self.array[mid] > self.array[mid+1]:
                    print("Peak element: ", self.array[mid])
                    return
            elif mid == len(self.array) - 1:
                if self.array[mid] > self.array[mid-1]:
                    print("Peak element: ", self.array[mid])
                    return
            elif self.array[mid] > self.array[mid+1] and self.array[mid] > self.array[mid-1]:
                print("Peak element: ", self.array[mid])
                return
            elif self.array[mid-1] > self.array[mid]:
                return self.peakBinarySearch(low, mid-1)
            elif self.array[mid+1] > self.array[mid]:
                return self.peakBinarySearch(mid+1, high)
    
    def getPeakElement(self):
        self.peakBinarySearch(0, len(self.array))


array = [1,2,3,4,5,6,7,8,9,0]
obj = FindingPeakElement(array)
obj.getPeakElement()
