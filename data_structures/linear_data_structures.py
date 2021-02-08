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
    def __init__(self,initdata):
        self.data = initdata
        self.next = None

    def getData(self):
        return self.data

    def getNext(self):
        return self.next

    def setData(self,newdata):
        self.data = newdata

    def setNext(self,newnext):
        self.next = newnext


class Node:
    def __init__(self, initial_data):
        self.data = initial_data
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
        temporary_node = Node(item_in)
        temporary_node.set_next(self.head)
        self.head = temporary_node

    def remove(self, item_in):
        current_item = self.head
        previous_item = None
        found = False
        while not found:
            if current_item.get_data() == item_in:
                found = True
            else:
                previous_item = current_item
                current_item = current_item.get_next()
        if previous_item is None:
            self.head = current_item.get_next()
        else:
            previous_item.set_next(current_item.get_next())

    def search(self, item_in):
        current_item = self.head
        is_found = False
        while current_item is not None and not is_found:
            if current_item.get_data() == item_in:
                is_found = True
            else:
                current_item = current_item.get_next()
        return is_found

    def is_empty(self):
        return self.head is None

    def size(self):
        current_item = self.head
        count = 0
        while current_item is not None:
            count = count + 1
            current_item = current_item.get_next()
        return count

    def append(self, item_in):
        current_item = self.head
        temporary_node = Node(item_in)
        while current_item.get_next() is not None:
            current_item = current_item.get_next()
        current_item.set_next(temporary_node)

    def index(self, item_in):
        current_item = self.head
        index = 0
        while current_item is not None and current_item.get_data() != item_in:
            current_item = current_item.get_next()
            index += 1
        return index

    def insert(self, index_in, item_in):
        count = index_in
        new_item = Node(item_in)
        current_item = self.head
        previous_item = None
        while count != 0:
            previous_item = current_item
            current_item = current_item.get_next()
            count -= 1
        previous_item.set_next(new_item)
        new_item.set_next(current_item)

    def pop(self):
        current_item = self.head
        previous_item = None
        if current_item.get_next() is None:
            self.head = None
            return current_item.get_data()
        while current_item.get_next() is not None:
            previous_item = current_item
            current_item = current_item.get_next()
        previous_item.set_next(None)
        return current_item.get_data()

    # def pop(self, index_in):
    #     count = index_in
    #     current_item = self.head
    #     previous_item = None
    #     if index_in == 0:
    #         self.head = current_item.get_next()
    #         return current_item.get_data()
    #     while count != 0:
    #         previous_item = current_item
    #         current_item = current_item.get_next()
    #         count -= 1
    #     previous_item.set_next(current_item.get_next())
    #     return current_item.get_data()


class OrderedList:
    def __init__(self):
        self.head = None

    def add(self, item_in):
        current_item = self.head
        previous_item = None
        stop = False
        while current_item is not None and not stop:
            if current_item.get_data() > item_in:
                stop = True
            else:
                previous_item = current_item
                current_item = current_item.get_next()

        temporary_node = Node(item_in)
        if previous_item is None:
            temporary_node.set_next(self.head)
            self.head = temporary_node
        else:
            temporary_node.set_next(current_item)
            previous_item.set_next(temporary_node)

    def remove(self, item_in):
        current_item = self.head
        previous_item = None
        found = False
        while not found:
            if current_item.get_data() == item_in:
                found = True
            else:
                previous_item = current_item
                current_item = current_item.get_next()
        if previous_item is None:
            self.head = current_item.get_next()
        else:
            previous_item.set_next(current_item.get_next())

    def search(self, item_in):
        current_item = self.head
        is_found = False
        stop = False
        while current_item is not None and not is_found and not stop:
            if current_item.get_data() == item_in:
                is_found = True
            else:
                if current_item.get_data() > item_in:
                    stop = True
                else:
                    current_item = current_item.get_next()
        return is_found

    def is_empty(self):
        return self.head is None

    def size(self):
        current_item = self.head
        count = 0
        while current_item is not None:
            count = count + 1
            current_item = current_item.get_next()
        return count

    def index(self, item_in):
        current_item = self.head
        index = 0
        while current_item is not None and current_item.get_data() != item_in:
            current_item = current_item.get_next()
            index += 1
        return index

    def pop(self):
        current_item = self.head
        previous_item = None
        if current_item.get_next() is None:
            self.head = None
            return current_item.get_data()
        while current_item.get_next() is not None:
            previous_item = current_item
            current_item = current_item.get_next()
        previous_item.set_next(None)
        return current_item.get_data()

    # def pop(self, index_in):
    #     count = index_in
    #     current_item = self.head
    #     previous_item = None
    #     if index_in == 0:
    #         self.head = current_item.get_next()
    #         return current_item.get_data()
    #     while count != 0:
    #         previous_item = current_item
    #         current_item = current_item.get_next()
    #         count -= 1
    #     previous_item.set_next(current_item.get_next())
    #     return current_item.get_data()
