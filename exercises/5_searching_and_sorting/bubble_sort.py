def bubble_sort(list_in):
    while True:
        is_ready = True
        index = 0
        while index < len(list_in) - 1:
            if list_in[index] > list_in[index + 1]:
                list_in[index], list_in[index + 1] = list_in[index + 1], list_in[index]
                is_ready = False
            index += 1
        if is_ready:
            break
    return list_in
