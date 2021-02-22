def sequential_search(list_in, item_in):
    index = 0
    while index < len(list_in):
        if list_in[index] == item_in:
            return True
        index += 1
    return False


my_list = [1, 3, 2]

print(sequential_search(my_list, 0))
