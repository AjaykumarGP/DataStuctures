

# Rearrange an array such that arr[i] = i



array = [-1, -1, 6, 1, 9,
           -1, 3, -1, 4, -1]


# setContainer = set()
# for i in range(0, len(array)):
#     setContainer.add(array[i])

# for i in range(0, len(array)):
#     if i in setContainer:
#         print(i, end=" ")
#     else:
#         print(-1, end=" ")

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Method - 2 (Swap operations)

i=0
while(i<len(array)):
    
    if array[i] >= 0 and array[i] != i:
        array[array[i]], array[i] = array[i], array[array[i]]
    else:
        i = i+1

print(array)

#Time complexity = O(n)
#Auxiliary space complexity = O(1)
