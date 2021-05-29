

#Reversal algorithm for array rotation

def reverse(array, start, end):
    
    while(start<end):
        
        temp = array[start]
        array[start]= array[end]
        array[end] = temp
        start += 1
        end -= 1

def rotate(array, numberOfRotation):
    if numberOfRotation == 0:
        return array
    
    numberOfRotation = numberOfRotation % len(array)
   
    reverse(array, 0, numberOfRotation-1)
    reverse(array, numberOfRotation, len(array)-1)
    reverse(array, 0, len(array)-1)

    print(array)


array = [1,2,3,4,5,6,7]
numberOfRotation = 2

rotate(array, numberOfRotation)
