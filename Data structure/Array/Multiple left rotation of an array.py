





# Quickly find multiple left rotations of an array | Set 1

def rotateArrayFirst(array, rotationKey, key): #Time complexity = O(2n), but Auxiliary space complexity = O(2n) 

    tempArray = [array[i%len(array)] for i in range(0, 2*len(array))] #Time complexity = O(2n)
    for i in rotationKey:
        print(tempArray[i%len(array):i%len(array)+len(array)]) #Time complexity = O(1)
    
def rotateArraySecond(array, rotationKey, key): #Time complexity = O(n), Auxiliary space coomplexity = O(1)
    for i in rotationKey:
        for j in range(i, i+len(array)):
            print(array[j%len(array)], end=" ")
        print(end="\n")



def incipient():
    
    array = [1,3,5,7,9]
    rotationKey = [1,3,4,6]
    
    rotateArrayFirst(array, rotationKey, 1)
    rotateArraySecond(array, rotationKey, 2)
    





#Driver code
if __name__ == "__main__":
    incipient()

