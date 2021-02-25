from data_structures.binary_tree import *

"""
Write a function that returns a tree using the list of lists functions that looks like this:

            a
    b               c
        d       e       f
"""


def build_tree():
    root = binary_tree("a")
    insert_left(root, "b")
    insert_right(root, "c")
    b = get_left_child(root)
    c = get_right_child(root)
    insert_right(b, "d")
    insert_left(c, "e")
    insert_right(c, "f")
    return root


print(build_tree())
