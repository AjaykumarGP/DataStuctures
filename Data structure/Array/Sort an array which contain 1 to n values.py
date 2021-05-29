



#Sort the given array which contains 1 to n


class SortArray():
    def __init__(self, array):
        self.array = array

    def sortArray(self):
        for i in range(0, len(self.array)):
            self.array[i] = i + 1

    def printSortedArray(self):
        print(self.array)


array = [10, 7, 9, 2, 8, 3, 5, 4, 6, 1]
obj = SortArray(array)
obj.sortArray()
obj.printSortedArray()
