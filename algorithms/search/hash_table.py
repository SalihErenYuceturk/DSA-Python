class HashTable:
    def __init__(self, size_in):
        self.size = size_in
        self.slots = [None] * self.size
        self.data = [None] * self.size

    def put(self, key_in, value_in):
        hash_value = self.hash_function(key_in, len(self.slots))
        if self.slots[hash_value] is None:
            self.slots[hash_value] = key_in
            self.data[hash_value] = value_in
        else:
            if self.slots[hash_value] == key_in:
                self.data[hash_value] = value_in
            else:
                next_slot = self.rehash(hash_value, len(self.slots))
                while self.slots[next_slot] is not None and self.slots[next_slot] != key_in:
                    next_slot = self.rehash(next_slot, len(self.slots))
                if self.slots[next_slot] is None:
                    self.slots[next_slot] = key_in
                    self.data[next_slot] = value_in
                else:
                    self.data[next_slot] = value_in

    # The hash function can be changed. This is a simple implementation. The hash value is calculated as key mod size
    # of value.
    def hash_function(self, key_in, size_in):
        return key_in % size_in

    def rehash(self, old_hash_in, size_in):
        return (old_hash_in + 1) % size_in

    def get(self, key_in):
        start_slot = self.hash_function(key_in, len(self.slots))
        data = None
        found = False
        position = start_slot
        while self.slots[position] is not None and not found:
            if self.slots[position] == key_in:
                found = True
                data = self.data[position]
            else:
                position = self.rehash(position, len(self.slots))
                if position == start_slot:
                    break
        return data

    def __getitem__(self, key_in):
        return self.get(key_in)

    def __setitem__(self, key_in, value_in):
        self.put(key_in, value_in)
