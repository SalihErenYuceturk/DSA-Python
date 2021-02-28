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
