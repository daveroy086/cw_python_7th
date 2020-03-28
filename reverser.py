def countLeadingZeros(aFloat):
    import math
    
    if math.modf(aFloat)[1] != 0:
        aCounter = -1 
        return aCounter

    else:
        aCounter = countLeadingZeros(aFloat * 10)
        aCounter += 1
    return aCounter
    
def reverse(aNumber):
    print("aNumber is ", aNumber)
    
    """Returns aNumber with all digits reversed. Assume positive aNumber."""

    #get the length of aNumber without using len()
    getANumberLength = aNumber
    length = 0
    while getANumberLength > 10 :
        getANumberLength  = getANumberLength / 10
        length += 1
    
    print("length is ", length)

    # when reverser is called with a one digit number return it  #base case
    if length < 1:    #the real length is  = 1 but aNumber never goes into the 
                      # while, so the variable 'length' never gets incremented
        print("base case returns: ", aNumber)
        return aNumber

    #get the modulo of aNumber using an exponent of ten to get a number between 1 and 10
    # use modf to get the integer and decimal parts
    import math

    firstDigit = math.modf(aNumber / (10**length))[1]
    print("firstDigit is " , firstDigit)
    decimalPart = math.modf(aNumber / (10**length))[0]
    print("decimalPart is ", decimalPart)

    #I need a loop that detects trialing zeros and adds them to firstDigit
    #before reverse is called
    zerosToAdd = 0
    if (decimalPart * 10) < 1:
        zerosToAdd = countLeadingZeros(decimalPart)
        print ("firstDigit is", firstDigit)

    # save the int for when the recursive call of reverser returns
    # return the decimal part of modf to an int
    # call reverser with this int
    returnedNumber = reverse(round(decimalPart, length)* (10**(length)))
    if zerosToAdd != 0:
        returnedNumber = (returnedNumber * (10**zerosToAdd))
    print("retirned number is ", returnedNumber)

    return ((returnedNumber * 10) +firstDigit)
    
    # multiply the returned number by ten and add the saved int from the beginning of the recursive call/frame
    # return this number


print(reverse(1234))#, 4321)
print(reverse(12045))#, 78901)
#print(reverse(1020))#, 201)

"""     if zerosToAdd != 0:
        returnedNumber * (10**zerosToAdd) """
