def shell_sort(list_in):
    sublist_count = len(list_in) // 2
    while sublist_count > 0:
        for start_position in range(sublist_count):
            gap_insertion_sort(list_in, start_position, sublist_count)
        print("after increments of size_in", sublist_count, "the list is", list_in)
        sublist_count = sublist_count // 2


def gap_insertion_sort(list_in, start, gap):
    for i in range(start + gap, len(list_in), gap):
        current_value = list_in[i]
        position = i
        while position >= gap and list_in[position - gap] > current_value:
            list_in[position] = list_in[position - gap]
            position = position-gap
        list_in[position] = current_value


my_list = [54, 26, 93, 17, 77, 31, 44, 55, 20]
shell_sort(my_list)
print(my_list)
