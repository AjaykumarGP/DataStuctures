




#Sort an array of 0s, 1s and 2s

#1. Three pointer for three partition problem
#2. Lomuto partition scheme for two pointer forward marching 



def rearrange(array):
    low = 0
    mid = 0
    high = len(array)-1

    while(mid <= high):
        
        if(array[mid] == 0):
            array[low], array[mid] = array[mid], array[low]
            mid += 1
            low += 1

        elif array[mid] == 1:
            mid += 1
        
        elif array[mid] == 2 :
            array[mid], array[high] = array[high], array[mid]
            high -= 1
        
        print(array)
    


array = [0, 1, 1, 0, 1, 2, 1, 2, 0, 0, 0, 1]

rearrange(array)
