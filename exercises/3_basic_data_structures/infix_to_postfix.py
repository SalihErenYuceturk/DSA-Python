from data_structures.linear.stack import *


def infix_to_postfix(string_in):
    precedence = {"*": 3, "/": 3, "+": 2, "-": 2, "(": 1}
    operators = "+-*/"
    operands = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    operator_stack = Stack()
    infix_list = string_in.split(" ")
    postfix_list = []
    for element in infix_list:
        if element in operands:
            postfix_list.append(element)
        elif element in "(":
            operator_stack.push(element)
        elif element in ")":
            while True:
                pop = operator_stack.pop()
                if pop == "(":
                    break
                postfix_list.append(pop)
        if element in operators:
            while (not operator_stack.is_empty()) and (precedence[operator_stack.peek()] >= precedence[element]):
                postfix_list.append(operator_stack.pop())
            operator_stack.push(element)
    while True:
        if operator_stack.is_empty():
            break
        postfix_list.append(operator_stack.pop())
    return " ".join(postfix_list)


def postfix_evaluation(string_in):
    operands = "0123456789"
    operators = "+-*/"
    postfix_list = string_in.split(" ")
    operand_stack = Stack()
    for element in postfix_list:
        if element in operands:
            operand_stack.push(element)
        if element in operators:
            a = operand_stack.pop()
            b = operand_stack.pop()
            if element == "*":
                c = int(b) * int(a)
            elif element == "/":
                c = int(b) / int(a)
            elif element == "-":
                c = int(b) - int(a)
            elif element == "+":
                c = int(b) + int(a)
            operand_stack.push(c)
    return operand_stack.pop()


# print(infix_to_postfix("10 + 3 * 5 / (16 - 4)"))
# print(infix_to_postfix("( A + B ) * C - ( D - E ) * ( F + G )"))
# print(postfix_evaluation("7 8 + 3 2 + /"))
