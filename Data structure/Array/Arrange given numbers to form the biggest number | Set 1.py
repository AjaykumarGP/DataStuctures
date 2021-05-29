


#Arrange given numbers to form the biggest number | Set 1

from itertools import permutations

def getLargestPossibleArrangement(array):
    
    possibleOutcomes = []
    for i in permutations(array, len(array)): #Permutation([array], [length of array])
        possibleOutcomes.append("".join(map(str, i)))
    
    return max(possibleOutcomes)

array = [54, 546, 548, 60]
print(getLargestPossibleArrangement(array))
