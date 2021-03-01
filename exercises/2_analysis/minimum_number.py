"""
Write two Python functions to find the minimum value in a list.

1. Compare each value to every other value on the list. O(n^2).

2. Find the minimum item_in with linear complexity. O(n).
"""


def minimum_squared(list_in):
    minimum = list_in[0]
    for search_number in list_in:
        for scan_number in list_in:
            if search_number > scan_number and scan_number < minimum:
                minimum = scan_number
    return minimum


def minimum_linear(list_in):
    minimum = list_in[0]
    for number in list_in:
        if number < minimum:
            minimum = number
    return minimum
