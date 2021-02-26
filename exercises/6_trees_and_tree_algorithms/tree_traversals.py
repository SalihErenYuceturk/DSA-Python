import operator


def preorder(tree_in):
    if tree_in:
        print(tree_in.get_root())
        preorder(tree_in.get_left_child())
        preorder(tree_in.get_right_child())


def postorder(tree_in):
    if tree_in is not None:
        postorder(tree_in.get_left_child())
        postorder(tree_in.get_right_child())
        print(tree_in.get_root())


def postorder_evaluate(tree_in):
    operations = {"+": operator.add, "-": operator.sub, "*": operator.mul, "/": operator.truediv}
    result1 = None
    result2 = None
    if tree_in:
        result1 = postorder_evaluate(tree_in.get_left_child())
        result2 = postorder_evaluate(tree_in.get_right_child())
        if result1 and result2:
            return operations[tree_in.get_root()](result1, result2)
        else:
            return tree_in.get_root()


def inorder(tree_in):
    if tree_in is not None:
        inorder(tree_in.get_left_child())
        print(tree_in.get_root())
        inorder(tree_in.get_right_child())


def print_expression(tree_in):
    string = ""
    if tree_in:
        string = "(" + print_expression(tree_in.get_left_child())
        string = string + str(tree_in.get_root())
        string = string + print_expression(tree_in.get_right_child()) + ")"
    return string
