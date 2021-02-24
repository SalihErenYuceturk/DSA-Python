def quick_sort(list_in):
    quick_sort_helper(list_in, 0, len(list_in) - 1)


def quick_sort_helper(list_in, first, last):
    if first < last:
        split_point = partition(list_in, first, last)

        quick_sort_helper(list_in, first, split_point - 1)
        quick_sort_helper(list_in, split_point + 1, last)


def partition(list_in, first, last):
    pivot_value = list_in[first]
    left_mark = first+1
    right_mark = last
    done = False
    while not done:
        while left_mark <= right_mark and list_in[left_mark] <= pivot_value:
            left_mark = left_mark + 1
        while list_in[right_mark] >= pivot_value and right_mark >= left_mark:
            right_mark = right_mark - 1
        if right_mark < left_mark:
            done = True
        else:
            temp = list_in[left_mark]
            list_in[left_mark] = list_in[right_mark]
            list_in[right_mark] = temp
    temp = list_in[first]
    list_in[first] = list_in[right_mark]
    list_in[right_mark] = temp
    return right_mark
