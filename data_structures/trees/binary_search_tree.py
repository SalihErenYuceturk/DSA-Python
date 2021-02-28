class TreeNode:
    def __init__(self, key_in, value_in, left=None, right=None, parent=None):
        self.key = key_in
        self.payload = value_in
        self.left_child = left
        self.right_child = right
        self.parent = parent

    def has_left_child(self):
        return self.left_child

    def has_right_child(self):
        return self.right_child

    def is_left_child(self):
        return self.parent and self.parent.left_child == self

    def is_right_child(self):
        return self.parent and self.parent.right_child == self

    def is_root(self):
        return not self.parent

    def is_leaf(self):
        return not (self.right_child or self.left_child)

    def has_any_children(self):
        return self.right_child or self.left_child

    def has_both_children(self):
        return self.right_child and self.left_child

    def splice_out(self):
        if self.is_leaf():
            if self.is_left_child():
                self.parent.left_child = None
            else:
                self.parent.right_child = None
        elif self.has_any_children():
            if self.has_left_child():
                if self.is_left_child():
                    self.parent.left_child = self.left_child
                else:
                    self.parent.right_child = self.left_child
                self.left_child.parent = self.parent
            else:
                if self.is_left_child():
                    self.parent.left_child = self.right_child
                else:
                    self.parent.right_child = self.right_child
                self.right_child.parent = self.parent

    def find_successor(self):
        successor = None
        if self.has_right_child():
            successor = self.right_child.find_min()
        else:
            if self.parent:
                if self.is_left_child():
                    successor = self.parent
                else:
                    self.parent.right_child = None
                    successor = self.parent.find_successor()
                    self.parent.right_child = self
        return successor

    def find_min(self):
        current = self
        while current.has_left_child():
            current = current.left_child
        return current

    def replace_node_data(self, key_in, value_in, left_child_in, right_child_in):
        self.key = key_in
        self.payload = value_in
        self.left_child = left_child_in
        self.right_child = right_child_in
        if self.has_left_child():
            self.left_child.parent = self
        if self.has_right_child():
            self.right_child.parent = self


class BinarySearchTree:
    def __init__(self):
        self.root = None
        self.size = 0

    def length(self):
        return self.size

    def __len__(self):
        return self.size

    def put(self, key_in, value_in):
        if self.root:
            self._put(key_in, value_in, self.root)
        else:
            self.root = TreeNode(key_in, value_in)
        self.size = self.size + 1

    def _put(self, key_in, value_in, current_node_in):
        if key_in < current_node_in.key:
            if current_node_in.has_left_child():
                self._put(key_in, value_in, current_node_in.left_child)
            else:
                current_node_in.left_child = TreeNode(key_in, value_in, parent=current_node_in)
        else:
            if current_node_in.has_right_child():
                self._put(key_in, value_in, current_node_in.right_child)
            else:
                current_node_in.right_child = TreeNode(key_in, value_in, parent=current_node_in)

    def __setitem__(self, key_in, value_in):
        self.put(key_in, value_in)

    def get(self, key_in):
        if self.root:
            res = self._get(key_in, self.root)
            if res:
                return res.payload
            else:
                return None
        else:
            return None

    def _get(self, key_in, current_node_in):
        if not current_node_in:
            return None
        elif current_node_in.key == key_in:
            return current_node_in
        elif key_in < current_node_in.key:
            return self._get(key_in, current_node_in.left_child)
        else:
            return self._get(key_in, current_node_in.right_child)

    def __getitem__(self, key_in):
        return self.get(key_in)

    def __contains__(self,  key):
        if self._get(key, self.root):
            return True
        else:
            return False

    def delete(self, key_in):
        if self.size > 1:
            nodeToRemove = self._get(key_in, self.root)
            if nodeToRemove:
                self.remove(nodeToRemove)
                self.size = self.size-1
            else:
                raise KeyError('Error, key_in not in tree')
        elif self.size == 1 and self.root.key == key_in:
            self.root = None
            self.size = self.size - 1
        else:
            raise KeyError('Error, key_in not in tree')

    def __delitem__(self, key_in):
        self.delete(key_in)

    def remove(self, current_node_in):
        if current_node_in.is_leaf():  # leaf
            if current_node_in == current_node_in.parent.left_child:
                current_node_in.parent.left_child = None
            else:
                current_node_in.parent.right_child = None
        elif current_node_in.has_both_children():  # interior
            successor = current_node_in.find_successor()
            successor.splice_out()
            current_node_in.key = successor.key
            current_node_in.payload = successor.payload

        else:
            if current_node_in.has_left_child():
                if current_node_in.is_left_child():
                    current_node_in.left_child.parent = current_node_in.parent
                    current_node_in.parent.left_child = current_node_in.left_child
                elif current_node_in.is_right_child():
                    current_node_in.left_child.parent = current_node_in.parent
                    current_node_in.parent.right_child = current_node_in.left_child
                else:
                    current_node_in.replace_node_data(current_node_in.left_child.key, current_node_in.left_child.payload,
                                                      current_node_in.left_child.left_child, current_node_in.left_child.right_child)
            else:
                if current_node_in.is_left_child():
                    current_node_in.right_child.parent = current_node_in.parent
                    current_node_in.parent.left_child = current_node_in.right_child
                elif current_node_in.is_right_child():
                    current_node_in.right_child.parent = current_node_in.parent
                    current_node_in.parent.right_child = current_node_in.right_child
                else:
                    current_node_in.replace_node_data(current_node_in.right_child.key, current_node_in.right_child.payload,
                                                      current_node_in.right_child.left_child, current_node_in.right_child.right_child)

