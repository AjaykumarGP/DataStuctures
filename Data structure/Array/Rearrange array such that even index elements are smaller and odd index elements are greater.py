




# Rearrange array such that even index elements are smaller and odd index elements are greater

def rearrange(array):
    for i in range(0, len(array)-1):
        if i%2 == 0:
            if array[i] > array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
        else:
            if array[i] < array[i+1]:
                array[i], array[i+1] = array[i+1], array[i]
    print(array)

array = [5, 4, 3, 6, 8, 7]


rearrange(array)
