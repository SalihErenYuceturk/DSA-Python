def sequential_search(list_in, item_in):
    index = 0
    while index < len(list_in):
        if list_in[index] == item_in:
            return True
        index += 1
    return False
