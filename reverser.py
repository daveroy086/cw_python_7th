def reverse(aNumber):
    
    """Returns aNumber with all digits reversed. Assume positive aNumber."""

    #get the length of aNumber without using len()
    getANumberLength = aNumber
    length = 0
    while getANumberLength > 10 :
        getANumberLength  = getANumberLength / 10
        length += 1

    # when reverser is called with a one digit number return it  #base case
    if length < 1:    #the real length is  = 1 but aNumber never goes into the 
                      # while so the variable 'length' never gets incremented
        return aNumber

    #get the modulo of aNumber using an exponent of ten to get a number between 1 and 10
    # use modf to get the integer and decimal parts
    import math
    firstDigit = math.modf(aNumber / (10**length))[1]
    decimalPart = math.modf(aNumber / (10**length))[0]

    # save the int for when the recursive call of reverser returns
    # return the decimal part of modf to an int
    # call reverser with this int
    returnedNumber = reverse(round(decimalPart, length)* (10**(length)))
    return ((returnedNumber * 10) +firstDigit)
    
    # multiply the returned number by ten and add the saved int from the beginning of the recursive call/frame
    # return this number


print(reverse(1234))
#, 4321)

#print(reverse(10987))#, 78901)
#print(reverse(1020))#, 201)

"""
    #use modf to get the integer and decimal parts
    #save them in varaibles
    #round the decimal part and multiply by ten to get an int
    #call reverser on the whole part
    #the base case returns the last whole number
    #mutiply the returned number by ten
    #add the saved int from earlier
    # return that
  
      holderArray = []

    if(len(str(abs(aNumber))) == 1):    #base case
        return aNumber

        holderArray.append(aNumber % 10)
        reverse(aNumber // 10, outputArray, holderArray)
        print(outputArray)
        return outputArray
 """
