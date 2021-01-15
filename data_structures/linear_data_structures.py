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
