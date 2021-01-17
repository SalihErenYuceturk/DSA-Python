from data_structures.linear_data_structures import Queue


def hot_potato(name_list_in, number_in):
    circle = Queue()
    for name in name_list_in:
        circle.enqueue(name)
    while True:
        number = number_in
        if circle.size() == 1:
            break
        while number > 0:
            top_name = circle.dequeue()
            circle.enqueue(top_name)
            number -= 1
        circle.dequeue()
    return circle.dequeue()


# print(hot_potato(["Bill","David","Susan","Jane","Kent","Brad"],7)) => Prints Susan
