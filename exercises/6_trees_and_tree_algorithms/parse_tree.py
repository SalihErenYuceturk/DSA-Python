from data_structures.linear_data_structures import Stack
from data_structures.binary_tree_nodes import BinaryTree
import operator

"""
1. If the current token is a '(', add a new node as the left child of the current node, and descend to the left child.
2. If the current token is in the list ['+','-','/','*'], set the root value of the current node to the operator 
represented by the current token. Add a new node as the right child of the current node and descend to the right child.
3. If the current token is a number, set the root value of the current node to the number and return to the parent.
4. If the current token is a ')', go to the parent of the current node.
"""


def build_parse_tree(expression_in):
    character_list = expression_in.split()
    stack = Stack()
    tree = BinaryTree("")
    stack.push(tree)
    current_tree = tree
    for i in character_list:
        if i == "(":
            current_tree.insert_left("")
            stack.push(current_tree)
            current_tree = current_tree.get_left_child()
        elif i in ["+", "-", "*", "/"]:
            current_tree.set_root(i)
            current_tree.insert_right("")
            stack.push(current_tree)
            current_tree = current_tree.get_right_child()
        elif i == ")":
            current_tree = stack.pop()
        elif i not in ["+", "-", "*", "/", ")"]:
            current_tree.set_root(int(i))
            parent = stack.pop()
            current_tree = parent
    return tree


def evaluate(parse_tree_in):
    operators = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    left_child = parse_tree_in.get_left_child()
    right_child = parse_tree_in.get_right_child()
    if left_child and right_child:
        final_nodes = operators[parse_tree_in.get_root()]
        return final_nodes(evaluate(left_child), evaluate(right_child))
    else:
        return parse_tree_in.get_root()


parse_tree = build_parse_tree("( ( 10 + 5 ) * 3 )")
print(evaluate(parse_tree))
# parse_tree.postorder()
