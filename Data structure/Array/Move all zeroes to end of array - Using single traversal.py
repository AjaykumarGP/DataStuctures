



# #Move all zeroes to end of array
## Method - 1


# def moveAllZeros(array):
#     count = 0
#     index = 0
#     while(index < len(array)-1):
#         if array[index] != 0:
#             array[count] = array[index]
#             index += 1
#             count += 1
#         else: index += 1
    
#     for i in range(count, len(array)-1):
#         array[i] = 0
#     return array

# array = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
# print(moveAllZeros(array))

#Method - 2 (Using single traversal)

def moveAllZeros2(array):
    count = 0
    index = 0
    while(index <= len(array)-1):
        if array[index] != 0:
            array[count], array[index] = array[index], array[count]
            index += 1
            count += 1
        else: index += 1
    return array


secondArray = [1, 9, 8, 4, 0, 0, 2, 7, 0, 6, 0]
print(moveAllZeros2(secondArray))
