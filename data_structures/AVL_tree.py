from data_structures.binary_search_tree import *


class AVLTree(BinarySearchTree):
    def __init__(self):
        BinarySearchTree.__init__(self)

    def _put(self, key, val, current_node):
        if key < current_node.key:
            if current_node.hasLeftChild():
                self._put(key, val, current_node.left_child)
            else:
                current_node.left_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.left_child)
        else:
            if current_node.hasRightChild():
                self._put(key, val, current_node.right_child)
            else:
                current_node.right_child = TreeNode(key, val, parent=current_node)
                self.update_balance(current_node.right_child)

    def update_balance(self, node):
        if node.balanceFactor > 1 or node.balanceFactor < -1:
            self.rebalance(node)
            return
        if node.parent is not None:
            if node.isLeftChild():
                node.parent.balanceFactor += 1
            elif node.isRightChild():
                node.parent.balanceFactor -= 1
            if node.parent.balanceFactor != 0:
                self.update_balance(node.parent)

    def rotate_left(self, rotRoot):
        newRoot = rotRoot.rightChild
        rotRoot.rightChild = newRoot.left_child
        if newRoot.left_child is not None:
            newRoot.left_child.parent = rotRoot
        newRoot.parent = rotRoot.parent
        if rotRoot.isRoot():
            self.root = newRoot
        else:
            if rotRoot.isLeftChild():
                rotRoot.parent.left_child = newRoot
            else:
                rotRoot.parent.rightChild = newRoot
        newRoot.left_child = rotRoot
        rotRoot.parent = newRoot
        rotRoot.balanceFactor = rotRoot.balanceFactor + 1 - min(newRoot.balanceFactor, 0)
        newRoot.balanceFactor = newRoot.balanceFactor + 1 + max(rotRoot.balanceFactor, 0)

    def rebalance(self, node):
        if node.balanceFactor < 0:
            if node.rightChild.balanceFactor > 0:
                self.rotate_right(node.rightChild)
                self.rotate_left(node)
            else:
                self.rotate_left(node)
        elif node.balanceFactor > 0:
            if node.leftChild.balanceFactor < 0:
                self.rotate_left(node.leftChild)
                self.rotate_right(node)
            else:
                self.rotate_right(node)