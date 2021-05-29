

#Write a program to reverse an array or string

#Iterative approach

# def reverseArray(array):
#     print("Iterative approach")
#     start = 0
#     end = len(array)-1

#     while(start<end):
#         array[start], array[end] = array[end], array[start]
#         start += 1
#         end -= 1
#     return array

array = [1,2,3,4,5]

# print(reverseArray(array))

# ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

#Recursive approach

def recursiveSwap(array, start, end):

    if start < end:
        array[start], array[end] = array[end], array[start]
        return recursiveSwap(array, start+1, end-1)
    else:
        return
    

recursiveSwap(array, 0, len(array)-1)
print(array)
