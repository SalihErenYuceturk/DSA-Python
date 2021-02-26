from data_structures.binary_tree_lists import *
from data_structures.binary_tree_nodes import BinaryTree

"""
Write a function that returns a tree_in using the list of lists functions that looks like this:

            a
    b               c
        d       e       f
"""


def build_tree_list():
    root = binary_tree("a")
    insert_left(root, "b")
    insert_right(root, "c")
    b = get_left_child(root)
    c = get_right_child(root)
    insert_right(b, "d")
    insert_left(c, "e")
    insert_right(c, "f")
    return root


print(build_tree_list())


def build_tree_node():
    root = BinaryTree("a")
    root.insert_left("b")
    root.insert_right("c")

    b = root.get_left_child()
    b.insert_right("d")

    c = root.get_right_child()
    c.insert_left("e")
    c.insert_right("f")
    return root


tree = build_tree_node()
print(tree.get_right_child().get_root())
print(tree.get_left_child().get_root())
print(tree.get_left_child().get_right_child().get_root())
print(tree.get_right_child().get_left_child().get_root())
print(tree.get_right_child().get_right_child().get_root())
