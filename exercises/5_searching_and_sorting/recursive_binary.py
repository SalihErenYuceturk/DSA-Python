"""
Implement the binary search using recursion.
"""


def recursive_binary_search(list_in, item_in):
    if len(list_in) == 1 and list_in[0] != item_in:
        return False
    if len(list_in) >= 1:
        if list_in[len(list_in)//2] == item_in:
            return True
        elif list_in[len(list_in)//2] > item_in:
            list_in = list_in[:(len(list_in)//2)]
            return recursive_binary_search(list_in, item_in)
        elif list_in[len(list_in) // 2] < item_in:
            list_in = list_in[(len(list_in) // 2):]
            return recursive_binary_search(list_in, item_in)
