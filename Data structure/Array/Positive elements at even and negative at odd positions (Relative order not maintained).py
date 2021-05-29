





# Positive elements at even and negative at odd positions (Relative order not maintained)


def rearrange(array):
    j=0
    for i in range(0, len(array)):

        if j%2 != 0 and array[j] > 0:
            if array[i] > 0:
                continue
            array[i], array[j] = array[j], array[i]
        
        elif j%2 == 0 and array[j] < 0:
            if array[i] < 0:
                continue
            array[i], array[j] = array[j], array[i]
        j = j+1
    print(array)

array = [ 1, -3, 5, 6, -3, 6, 7, -4, 9, 10]

rearrange(array)

