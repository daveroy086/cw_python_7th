def countLeadingZeros(aFloat, length):
    import math

    if (math.modf(aFloat)[1] != 0) or (length == 1):
        aCounter = -1
        return aCounter

    else:
        aCounter = countLeadingZeros(aFloat * 10, length)
        aCounter += 1
    return aCounter

def reverse(aNumber):
    print("aNumber is ", aNumber)

    """Returns aNumber with all digits reversed. Assume positive aNumber."""

    getANumberLength = aNumber
    length = 0
    while getANumberLength > 10 :
        getANumberLength  = getANumberLength / 10
        length += 1

    print("length is ", length)

    if length < 1:    #the real length is  = 1 but aNumber never goes into the
                      # while, so the variable 'length' never gets incremented
        print("base case returns: ", aNumber)
        return aNumber

    import math

    firstDigit = math.modf(aNumber / (10**length))[1]
    print("firstDigit is " , firstDigit)
    decimalPart = math.modf(aNumber / (10**length))[0]
    print("decimalPart is ", decimalPart)

    zerosToAdd = 0
    if (decimalPart * 10) < 1:
        zerosToAdd = countLeadingZeros(decimalPart, length)
        print ("firstDigit is", firstDigit)

    returnedNumber = reverse(round(decimalPart, length)* (10**(length)))
    if zerosToAdd != 0:
        returnedNumber = (returnedNumber * (10**zerosToAdd))
    print("retirned number is ", returnedNumber)

    return ((returnedNumber * 10) +firstDigit)

#print(reverse(1234))#, 4321)
#print(reverse(12045))#, 78901)
print(reverse(1020))#, 201)
print(" the ans is ", reverse(1020))#, 201)
print(reverse(1001))#, 1001)
print(reverse(1010))#, he says 101 is ok)
