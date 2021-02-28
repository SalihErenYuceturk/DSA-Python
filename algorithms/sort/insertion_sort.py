def insertion_sort(list_in):
    for index in range(len(list_in)):
        current_value = list_in[index]
        while index > 0 and list_in[index - 1] > current_value:
            list_in[index] = list_in[index - 1]
            index = index - 1
        list_in[index] = current_value
    return list_in
