




# Find the element that appears once in a sorted array
# If the array is already sorted - use binary search search to find the anomly(Missing/Duplicate) element for O(Logn) complexity
# If the array is not already sorted - use XOR approach for O(n) complexity

class FindingOnceAppearingElement():
    def __init__(self, array):
        self.array = array
        self.arraySize = len(array)

    def binarySearch(self, low, high):
        if low <= high:
            mid = (low + high) // 2

            if mid == self.arraySize - 1:
                if self.array[mid] != self.array[mid-1]:
                    return self.array[mid]
            elif self.array[mid] != self.array[mid-1] and self.array[mid] != self.array[mid + 1]:
                return self.array[mid]
            elif mid % 2 == 0:
                if self.array[mid] == self.array[mid+1]:
                    return self.binarySearch(mid+1, high)
                else:
                    return self.binarySearch(low, mid-1)

            elif mid % 2 == 1:
                if self.array[mid] != self.array[mid-1]:
                    return self.binarySearch(low, mid-1)
                else:
                    return self.binarySearch(mid+1, high)

        print("No element appear once")
        return -1

    def findElement(self):
        result = self.binarySearch(0, len(self.array))
        
        print(result)

array = [1, 3, 3, 4, 4, 5, 5]
obj = FindingOnceAppearingElement(array)
obj.findElement()
