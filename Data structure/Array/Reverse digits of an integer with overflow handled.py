



# Reverse digits of an integer with overflow handled


import sys


def reverseInteger(integer):

    reverseValue = 0
    
    while(integer > 0):
        lastDigit = integer % 10
        if(reverseValue*10 > sys.maxsize or reverseValue*10 < -sys.maxsize): return 0, 0
        reverseValue = (reverseValue*10) + lastDigit
        integer = integer // 10
    return reverseValue, 1
    



integer = 45622

reverseValue, flag = reverseInteger(integer)

if flag == 0:
    print("Overflow occured")
else:
    print(reverseValue)
