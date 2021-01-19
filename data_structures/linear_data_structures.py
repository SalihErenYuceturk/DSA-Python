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

    def is_empty(self):
        return self.head is None

    def add(self, item_in):
        temp = Node(item_in)
        temp.set_next(self.head)
        self.head = temp

    def size(self):
        current = self.head
        count = 0
        while current is not None:
            count = count + 1
            current = current.get_next()
        return count

    def search(self, item_in):
        current = self.head
        found = False
        while current is not None and not found:
            if current.get_data() == item_in:
                found = True
            else:
                current = current.get_next()
        return found

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
