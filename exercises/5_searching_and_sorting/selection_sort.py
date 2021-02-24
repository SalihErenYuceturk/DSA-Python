def selection_sort(list_in):
    unordered_index = len(list_in) - 1
    while unordered_index != 0:
        index = 0
        max_value = list_in[0]
        max_index = 0
        while index <= unordered_index:
            if list_in[index] > max_value:
                max_value = list_in[index]
                max_index = index
            index += 1
        list_in[max_index], list_in[unordered_index] = list_in[unordered_index], list_in[max_index]
        unordered_index -= 1
    return list_in
