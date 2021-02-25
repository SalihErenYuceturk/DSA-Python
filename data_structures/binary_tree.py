def binary_tree(root):
    return [root, [], []]


def insert_left(root, new_branch):
    tree = root.pop(1)
    if len(tree) > 1:
        root.insert(1, [new_branch, tree, []])
    else:
        root.insert(1, [new_branch, [], []])
    return root


def insert_right(root, new_branch):
    tree = root.pop(2)
    if len(tree) > 1:
        root.insert(2, [new_branch, [], tree])
    else:
        root.insert(2, [new_branch, [], []])
    return root


def get_root(root):
    return root[0]


def set_root(root, new_value):
    root[0] = new_value


def get_left_child(root):
    return root[1]


def get_right_child(root):
    return root[2]