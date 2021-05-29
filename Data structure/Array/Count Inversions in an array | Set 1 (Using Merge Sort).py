

#Count Inversions in an array | Set 1 (Using Merge Sort)

class MergeSort():

    def __init__(self):
        self.InversionCounter = 0
    
    def mergeSort(self, array):
         
        if len(array) > 1:
            mid = len(array) // 2

            leftPartition = array[:mid]
            rightPartition = array[mid:]

            self.mergeSort(leftPartition)
            self.mergeSort(rightPartition)

            i=j=k = 0
            
            while(i<len(leftPartition) and j < len(rightPartition)):
                if leftPartition[i] > rightPartition[j]:
                    self.InversionCounter += len(leftPartition)-i
                    array[k] = rightPartition[j]
                    j += 1
                else:
                    array[k] = leftPartition[i]
                    i+= 1

                k += 1

            while(i<len(leftPartition)):
                array[k] = leftPartition[i]
                i += 1
                k += 1

            while(j<len(rightPartition)):
                array[k] = rightPartition[j]
                j += 1
                k += 1

            return array

class InversionCounter(MergeSort):
    def __init__(self, array):
        self.array = array
        MergeSort.__init__(self)

    def getInversionCount(self):
        result = self.mergeSort(self.array)
        print(result)
        print(self.InversionCounter)


array = [1, 20, 6, 4, 5]
obj = InversionCounter(array)
obj.getInversionCount()

