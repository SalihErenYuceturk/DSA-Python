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
