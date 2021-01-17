from data_structures.linear_data_structures import Deque


def is_palindrome(string_in):
    deque = Deque()
    for letter in string_in:
        deque.add_rear(letter)
    if deque.size() % 2 == 1:
        while True:
            if deque.size() == 1:
                break
            rear = deque.remove_rear()
            front = deque.remove_front()
            if rear != front:
                return False
    elif deque.size() % 2 == 0:
        while True:
            if deque.size() == 0:
                break
            rear = deque.remove_rear()
            front = deque.remove_front()
            if rear != front:
                return False
    return True


# print(is_palindrome("lsdkjfskf"))
# print(is_palindrome("radar"))
