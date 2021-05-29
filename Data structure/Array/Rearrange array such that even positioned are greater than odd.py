


#Rearrange array such that even positioned are greater than odd
#One other approach is to traverse the array from the second element and swap the element with the previous one if the condition is not satisfied.

def rearrangeArray(array):
    for i in range(1, len(array)):
        if i%2 != 0:
            #Even
            if array[i] > array[i-1]:
                continue
            else:
                array[i], array[i-1] = array[i-1], array[i]
        else:
            #Odd
            if array[i] < array[i-1]:
                continue
            else:
                array[i], array[i-1] = array[i-1], array[i]
    print(array)


array = [1, 3, 2, 2, 5]


rearrangeArray(array)
