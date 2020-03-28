def countLeadingZeros(aFloat, length):

    import math
    
    if (math.modf(aFloat)[1] != 0) or (length <= 2):
        print("math.modf(aFloat)[1] is ", math.modf(aFloat)[1], " and length is ", length)
        aCounter = -1 
        return aCounter

    #gives all correct answers but line 12 still gives infinite loop online
    # try wrapping line 12 in an if with length conditional 
    else:
        aCounter = countLeadingZeros(aFloat * 10, length)
        aCounter += 1
    return aCounter
    
def reverse(aNumber):
    #print("aNumber is ", aNumber)
    
    """Returns aNumber with all digits reversed. Assume positive aNumber."""

    getANumberLength = aNumber
    length = 0
    while getANumberLength > 10 :
        getANumberLength  = getANumberLength / 10
        length += 1

    if length < 1: 
        return aNumber

    import math

    firstDigit = math.modf(aNumber / (10**length))[1]
    decimalPart = math.modf(aNumber / (10**length))[0]

    zerosToAdd = 0
    if (decimalPart * 10) < 1:
        zerosToAdd = countLeadingZeros(decimalPart, length)

    returnedNumber = reverse(round(decimalPart, length)* (10**(length)))
    if zerosToAdd != 0:
        returnedNumber = (returnedNumber * (10**zerosToAdd - 1))

    iReturn = int((returnedNumber * 10) +firstDigit)
    #print("iReturn is ", iReturn)
    return iReturn

#print(reverse(1234))#, 4321)
#print(reverse(12045))#, 78901)
print(" the ans is ", reverse(1020))#, 201)
#print(reverse(1001))#, 1001)
#print(reverse(1010))#, he says 101 is ok)
""" 
import random
for i in range (10):
    numb = random.randrange(1000, 1000000000)
    print(i, "  for the number  ", numb, ", the reverse is ", reverse(numb))
 """
    #did not work for some test cases:
    #for the number   6003891 , it returned  1083006.0
    #for the number   78220351 , it returned  6302287.0
    #for the number   384427106 , it returned 7724483.000000001