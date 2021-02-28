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
