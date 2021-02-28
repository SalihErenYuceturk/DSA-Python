from data_structures.linear.stack import *

"""
Starting with an empty stack, process the parenthesis strings from left to right. If an element is "(", push it in 
the stack. If ana element is ")" pop the stack. If at the end the stack is not empty, the brackets are not balanced.
"""


def check_balance(string_in):
    balance = Stack()
    for element in string_in:
        if element == "(":
            balance.push("(")
        if element == ")" and not balance.is_empty():
            balance.pop()
        if element == ")" and balance.is_empty():
            return False
    return balance.is_empty()


# print(check_balance(")(()"))
