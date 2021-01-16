from data_structures.linear_data_structures import Stack

"""
Convert a decimal number to binary using divide by two and a stack. 
"""


# Returns the binary representation of an integer in base 10 greater than 0.
def decimal_to_binary(integer_in):
    stack = Stack()
    binary = ""
    while integer_in > 0:
        stack.push(integer_in % 2)
        integer_in = integer_in//2
    while not stack.is_empty():
        binary = binary + str(stack.pop())
    return binary


# Can choose up to base 16.
def decimal_to_base(integer_in, base_in):
    digits = "0123456789ABCDEF"
    stack = Stack()
    binary = ""
    while integer_in > 0:
        stack.push(digits[integer_in % base_in])
        integer_in = integer_in // base_in
    while not stack.is_empty():
        binary = binary + str(stack.pop())
    return binary


# print(decimal_to_base(256, 16))
