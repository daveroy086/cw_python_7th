def count_leading_zeros(a_float, length, count_leading_zeros_calls = 0):
  
    count_leading_zeros_calls += 1
  
    import math    
    
    if (math.modf(a_float)[1] != 0) and (count_leading_zeros_calls < original_length):
        print("math.modf(a_float)[1] is ", math.modf(a_float)[1], " and length is ", length)
        a_counter = -1 
        return a_counter
  
    #gives all correct answers but line 12 still gives infinite loop online
    # try wrapping line 12 in an if with length conditional 
    else:
        a_counter = count_leading_zeros(a_float * 10, length, count_leading_zeros_calls)
        a_counter += 1
    return a_counter
  
def reverse(a_number, count_reverse_calls = 0):
    count_reverse_calls += 1
    #print("a_number is ", a_number)
    
    """Returns a_number with all digits reversed. Assume positive a_number."""
  
    get_a_number_length = a_number
    length = 0
    original_length = 0
    while get_a_number_length > 10 :
        get_a_number_length  = get_a_number_length / 10
        length += 1
  
    if count_reverse_calls == 1:
        original_length = original_length
    if length < 1: 
        return a_number
  
    import math
  
    first_digit = math.modf(a_number / (10**length))[1]
    decimal_part = math.modf(a_number / (10**length))[0]
  
    zeros_to_add = 0
    if (decimal_part * 10) < 1:
        zeros_to_add = count_leading_zeros(decimal_part, length, original_length)
  
    returned_number = reverse(round(decimal_part, length), count_reverse_calls) * (10**length)
    if zeros_to_add != 0:
        returned_number = (returned_number * (10**zeros_to_add - 1))
  
    i_return = int((returned_number * 10) +first_digit)
    #print("i_return is ", i_return)
    return i_return
  
print(reverse(1234))#, 4321)
"""print(reverse(12045))#, 78901)
print(" the ans is ", reverse(1020))#, 201)
print(reverse(1001))#, 1001)
print(reverse(1010))#, he says 101 is ok)
"""
"""
import random
for i in range (10):
  numb = random.randrange(1000, 1000000000)
  print(i, "  for the number  ", numb, ", the reverse is ", reverse(numb))

  #did not work for some test cases:
  #print(reverse(6003891)) #1083006.0 is the wrong ans i received before
  #print(reverse(78220351)) #6302287 is the wrong ans i received before
  #print(reverse(384427106)) #7724483.000000001 is the wrong ans i received before
  """