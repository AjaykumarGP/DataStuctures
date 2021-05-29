


#Rearrange an array such that ‘arr[j]’ becomes ‘i’ if ‘arr[i]’ is ‘j’ | Set 1



def rearrangeArray(array):
    for i in range(0, len(array)):
        array[array[i]%len(array)] += i * len(array)
    print(array)
    
    for i in range(0, len(array)):
        print(array[i]//len(array), end=" ")


array = [2, 6, 0, 1, 4, 5, 3]

rearrangeArray(array)
