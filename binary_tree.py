class BinaryTree:
    def __init__(self, root):
        self.root = root

    def pre_order_traversal_recur(self, root):
        if root:
            print(root.data, end=' ')
            self.pre_order_traversal_recur(root.left)
            self.pre_order_traversal_recur(root.right)

    def in_order_traversal_recur(self, root):
        if root:
            self.in_order_traversal_recur(root.left)
            print(root.data)
            self.in_order_traversal_recur(root.right)

    def post_order_traversal_recur(self, root):
        if root:
            self.post_order_traversal_recur(root.left)
            self.post_order_traversal_recur(root.right)
            print(root.data)

    def height_of_tree_recur(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0
        else:
            return max(self.height_of_tree_recur(root.left), self.height_of_tree_recur(root.right)) + 1


class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

