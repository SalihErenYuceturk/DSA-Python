from algorithms.search.sequential_search import *
from algorithms.search.binary_search import *
from algorithms.sort.bubble_sort import *
import random
import time

"""
Set up a random experiment to test the difference between a sequential search and a binary search on a list of integers.
"""

list_length = 100
while list_length <= 10000:
    # Create a random unsorted list with a search value.
    test_list = []
    test_number = 0
    for i in range(list_length):
        value = 0
        while value in test_list:
            value = random.randrange(0, list_length + 1)
        test_list.append(value)
    test_number = test_list[random.randrange(len(test_list))]

    print()
    print("List Length: ", list_length)
    print("test_number: ", test_number)

    # Testing on the unsorted list for sequential.
    start_sequential = time.time()
    sequential_search(test_list, test_number)
    end_sequential = time.time()
    time_sequential = end_sequential - start_sequential

    print("Time for sequential sort (unsorted): ", time_sequential)

    test_list = bubble_sort(test_list)

    start_sequential = time.time()
    sequential_search(test_list, test_number)
    end_sequential = time.time()
    time_sequential = end_sequential - start_sequential

    start_binary = time.time()
    binary_search(test_list, test_number)
    end_binary = time.time()
    time_binary = end_binary - start_binary

    print("Time for sequential sort (sorted): ", time_sequential)
    print("Time for binary sort: ", time_binary)

    list_length = list_length * 10
