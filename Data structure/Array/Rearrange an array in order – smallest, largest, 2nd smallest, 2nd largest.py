

#Rearrange an array in order – smallest, largest, 2nd smallest, 2nd largest, ..



def mergeSort(array):
    if(len(array) > 1):
        mid = (len(array)) // 2

        leftPartition = array[:mid]
        rightParition = array[mid:]

        mergeSort(leftPartition)
        mergeSort(rightParition)

        i=j=k=0

        while(i<len(leftPartition) and j < len(rightParition)):
            if leftPartition[i] < rightParition[j]:
                array[k] = leftPartition[i]
                i+=1
                k+=1
            else:
                array[k] = rightParition[j]
                j+=1
                k+=1
        
        while(i<len(leftPartition)):
            array[k] = leftPartition[i]
            i+=1
            k+=1
        while(j<len(rightParition)):
            array[k] = rightParition[j]
            j+=1
            k+=1
    return array


def rearrangeArray(array, start, end):
    tempArray = [0 for i in range(0, len(array))]
    index = 0
    while(start<end):
        tempArray[index] = array[start]
        index += 1
        tempArray[index] = array[end] 
        index += 1

        start += 1
        end -= 1
    if len(array) % 2 !=0:
        tempArray[len(array)-1] = array[(len(array)-1) // 2]
    print(tempArray)
        


array = [5, 8, 1, 4, 2, 9, 3, 7, 6]

print(mergeSort(array))
rearrangeArray(array, 0, len(array)-1)



# Time complexity = O(n*logn)
# Space complexity = O(n)
