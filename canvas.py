
sum_list = [2, 4, 0, 8, 10]


def recursive_sum(list_in):
    if len(list_in) == 1:
        return list_in[0]
    else:
        return list_in[0] + recursive_sum(list_in[1:])


print(recursive_sum(sum_list))
