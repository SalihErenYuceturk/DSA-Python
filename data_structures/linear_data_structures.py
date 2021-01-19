class Stack:
    def __init__(self):
        self.items = []

    def push(self, item_in):
        self.items.append(item_in)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[-1]

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Queue:
    def __init__(self):
        self.items = []

    def enqueue(self, item_in):
        self.items.insert(0, item_in)

    def dequeue(self):
        return self.items.pop()

    def is_empty(self):
        return len(self.items) == 0

    def size(self):
        return len(self.items)


class Deque:
    def __init__(self):
        self.items = []

    def add_front(self, item_in):
        self.items.append(item_in)

    def add_rear(self, item_in):
        self.items.insert(0, item_in)

    def remove_front(self):
        return self.items.pop()

    def remove_rear(self):
        return self.items.pop(0)

    def is_empty(self):
        return self.items == []

    def size(self):
        return len(self.items)


class Node:
    def __init__(self, init_data):
        self.data = init_data
        self.next = None

    def get_data(self):
        return self.data

    def get_next(self):
        return self.next

    def set_data(self, new_data):
        self.data = new_data

    def set_next(self, new_next):
        self.next = new_next


class UnorderedList:
    def __init__(self):
        self.head = None

    def add(self, item_in):
        temp = Node(item_in)
        temp.set_next(self.head)
        self.head = temp

    def remove(self, item_in):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.get_data() == item_in:
                found = True
            else:
                previous = current
                current = current.get_next()
        if previous is None:
            self.head = current.get_next()
        else:
            previous.setNext(current.get_next())

    def search(self, item_in):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item_in:
                found = True
            else:
                current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count


"""
To Be Added:
append(item_in) - Add item_in to the front of the list. Assume item_in is not present in the list.
index(item_in) - Return the position of item_in in the list. Assume item_in is present in the list.
insert(index_in, item_in) - Add item_in to the list at index_in. Assume item_in is not present in the list.
pop() - Remove the front item from the list and return that item. Assume the list is not empty.
pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.
"""


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item_in):
        current = self.head
        previous = None
        stop = False
        while current is not None and not stop:
            if current.get_data() > item_in:
                stop = True
            else:
                previous = current
                current = current.get_next()
        temp = Node(item_in)
        if previous is None:
            temp.set_next(self.head)
            self.head = temp
        else:
            temp.set_next(current)
            previous.set_next(temp)

    def search(self, item_in):
        current = self.head
        found = False
        stop = False
        while current is not None and not found and not stop:
            if current.get_data() == item_in:
                found = True
            else:
                if current.get_data() > item_in:
                    stop = True
                else:
                    current = current.get_next()
        return found

    def is_empty(self):
        return self.head is None

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count


"""
To Be Added:
remove(item_in) - Remove item_in from the list. Assume item_in is present in the list.
index(item_in) - Return the position of item_in in the list. Assume item_in is present in the list.
pop() - Remove the front item from the list and return that item. Assume the list is not empty.
pop(index_in) - Remove and return the item at index_in. Assume the item is in the list.
"""