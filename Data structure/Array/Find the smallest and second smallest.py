




#Find the smallest and second smallest element in the array

import sys


array = [12, 13, 1, 10, 34, 1]
first = sys.maxsize
second = sys.maxsize
for i in range(0, len(array)):
    if array[i] <= first:
        second = first
        first = array[i]
    elif array[i] > first and array[i] < second:
        second = array[i]

print(first, second)
