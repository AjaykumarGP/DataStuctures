from collections import deque

array = [1,2,3,4,5]

array = deque(array)
array.rotate(-2) #Left rotation
array = list(array)
print(array)


