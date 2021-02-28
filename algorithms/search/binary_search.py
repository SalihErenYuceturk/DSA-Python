def binary_search(list_in, item_in):
    while len(list_in) >= 1:
        if list_in[len(list_in)//2] == item_in:
            return True
        elif list_in[len(list_in)//2] > item_in:
            list_in = list_in[:(len(list_in)//2)]
        elif list_in[len(list_in)//2] < item_in:
            list_in = list_in[(len(list_in)//2):]
    return False
