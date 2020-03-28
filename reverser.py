def countLeadingZeros(aFloat, length):
    import math
    
    aFloat = math.modf(aFloat)[1]
    if (math.modf(aFloat)[1] != 0) or (length == 1):
        aCounter = -1 
        return aCounter

    #gives all correct answers but line 10 still gives infinite loop 
    else:
        aCounter = countLeadingZeros(aFloat * 10, length)
        aCounter += 1
    return aCounter
    
def reverse(aNumber):
    
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
        returnedNumber = (returnedNumber * (10**zerosToAdd))

    return ((returnedNumber * 10) +firstDigit)
#print(reverse(1234))#, 4321)
#print(reverse(12045))#, 78901)
print(reverse(1020))#, 201)