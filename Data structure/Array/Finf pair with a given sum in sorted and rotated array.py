
#Given a sorted and rotated array, find if there is a pair with a given sum

def printArray(array):
    print(array)

def findPivotIndex(array):
    for i in range(0, len(array)):
        if(array[i] > array[i+1]):
            return i

def isPairInArray(array, sum):
    pivotIndex = findPivotIndex(array)
    greaterRange = pivotIndex
    smallerRange = (pivotIndex+1) % len(array)
    

    while(greaterRange != smallerRange):

        if(array[greaterRange] + array[smallerRange] == sum):
            return True
        
        if(array[greaterRange]+array[smallerRange] < sum):
            smallerRange = (smallerRange + 1) % len(array)
        else:
            greaterRange = (greaterRange - 1) % len(array)

def main():
    
    array = [4,5,6,7,1,2,3]
    sum = 12
    if(isPairInArray(array, sum)):
        print("PairFound")
    else:
        print("PairNotFound")
    printArray(array)

#Driver code
if __name__ == "__main__":
    main()


