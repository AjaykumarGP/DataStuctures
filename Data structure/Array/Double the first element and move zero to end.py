


#Double the first element and move zero to end Next




def changeOnCondition(array):
    for i in range(0, len(array)-1):
        if array[i] != 0 and array[i+1] != 0:
            array[i] = 2*array[i]
            array[i+1] = 0
    print(array)

def rearrange(array):
    #Two pointer approach
    count = 0
    index = 0
    while(index<len(array)):
        if(array[index] != 0):
            array[count], array[index] = array[index], array[count]
            index+=1
            count+=1
        else:
            index+=1
    print(array)



array = [2,2,0,4,0,8]

changeOnCondition(array)
rearrange(array)
