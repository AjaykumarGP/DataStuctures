




#Move all negative numbers to beginning and positive to end with constant extra space

def rearrange(array):
    start = 0
    end = len(array)-1

    while(start<end):
        if(array[start] < 0 and array[end] < 0):
            start += 1
        elif array[start] > 0 and array[end] >0:
            end -= 1
        elif(array[start] > 0 and array[end]<0):
            array[start], array[end] =array[end], array[start]
            start += 1
            end -=1
        else:
            start += 1
            end -= 1


    print(array)
            


array = [-1, 2, -3, 4, 5, 6, -7, 8, 9]
rearrange(array)
