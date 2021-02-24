def merge_sort(list_in):
    if len(list_in) > 1:
        middle = len(list_in) // 2
        left_half = list_in[:middle]
        right_half = list_in[middle:]
        merge_sort(left_half)
        merge_sort(right_half)
        i = 0
        j = 0
        k = 0
        while i < len(left_half) and j < len(right_half):
            if left_half[i] <= right_half[j]:
                list_in[k] = left_half[i]
                i = i + 1
            else:
                list_in[k] = right_half[j]
                j = j + 1
            k = k + 1
        while i < len(left_half):
            list_in[k] = left_half[i]
            i = i + 1
            k = k + 1
        while j < len(right_half):
            list_in[k] = right_half[j]
            j = j + 1
            k = k + 1
