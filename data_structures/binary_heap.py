class BinaryHeap:
    def __init__(self):
        self.heap_list = [0]
        self.current_size = 0

    def insert(self, item_in):
        self.heap_list.append(item_in)
        self.current_size = self.current_size + 1
        self.percolate_up(self.current_size)

    def delete_min(self):
        return_value = self.heap_list[1]
        self.heap_list[1] = self.heap_list[self.current_size]
        self.current_size = self.current_size - 1
        self.heap_list.pop()
        self.percolate_down(1)
        return return_value

    def build_heap(self, list_in):
        index = len(list_in) // 2
        self.current_size = len(list_in)
        self.heap_list = [0] + list_in[:]
        while index > 0:
            self.percolate_down(index)
            index = index - 1

    def percolate_up(self, index_in):
        while index_in // 2 > 0:
            if self.heap_list[index_in] < self.heap_list[index_in // 2]:
                tmp = self.heap_list[index_in // 2]
                self.heap_list[index_in // 2] = self.heap_list[index_in]
                self.heap_list[index_in] = tmp
            index_in = index_in // 2

    def percolate_down(self, index_in):
        while (index_in * 2) <= self.current_size:
            mc = self.min_child(index_in)
            if self.heap_list[index_in] > self.heap_list[mc]:
                tmp = self.heap_list[index_in]
                self.heap_list[index_in] = self.heap_list[mc]
                self.heap_list[mc] = tmp
            index_in = mc

    def min_child(self, index_in):
        if index_in * 2 + 1 > self.current_size:
            return index_in * 2
        else:
            if self.heap_list[index_in * 2] < self.heap_list[index_in * 2 + 1]:
                return index_in * 2
            else:
                return index_in * 2 + 1
