from data_structures.linear.stack import *


def check_balance(string_in):
    balance = Stack()
    open_brackets = "([{"
    close_brackets = ")]}"
    for element in string_in:
        if element in ")]}" and balance.is_empty():
            return False
        if element in "([{":
            balance.push(element)
        if element in ")]}":
            top = balance.pop()
            if open_brackets.index(top) != close_brackets.index(element):
                return False
    return True


# print(check_balance('{({([][])}())}'))
# print(check_balance('[{(})]'))

