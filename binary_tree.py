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

    def level_order_traversal_iter(self, root):
        queue = []
        queue.append(root)
        while queue:
            node = queue.pop(0)
            print(node.data, end=' ')
            if node.left:
                queue.append(node.left)
            if node.right:
                queue.append(node.right)

    def height_of_tree_recur(self, root):
        if root is None:
            return 0
        elif root.left is None and root.right is None:
            return 0
        else:
            return max(self.height_of_tree_recur(root.left), self.height_of_tree_recur(root.right)) + 1

    def topView(self, root):
        q = [root]
        top_map = {}
        root.level = 0
        while q:
            node = q.pop(0)
            if node.level not in top_map:
                top_map[node.level] = node.info
            if node.left:
                node.left.level = node.level - 1
                q.append(node.left)
            if node.right:
                node.right.level = node.level +1
                q.append(node.right)

        for i in sorted(top_map.keys()):
            print(top_map[i], end=' ')
    
    def insert(self, val):
        if not self.root:
            self.root = Node(val, None, None)
        else:
            node = self.root
            while True:
                if val > node.info:
                    if node.right is None:
                        node.right = Node(val, None, None)
                        break
                    else:
                        node = node.right
                else:
                    if node.left is None:
                        node.left = Node(val, None, None)
                        break
                    else:
                        node = node.left
        return self.root
    
    def lca(root, v1, v2):
        #Enter your code here
        v1_lst = []
        v2_lst = []
        for i,j in zip([v1,v2],[v1_lst, v2_lst]):
            node = root
            while True:
                j.append(node)
                if i == node.info:
                    break
                if i > node.info:
                    node = node.right
                else:
                    node = node.left
        n = min(len(v1_lst),len(v2_lst))
        for i in range(n):
            if v1_lst[i].info != v2_lst[i].info:
                if i > 0:
                    return v1_lst[i-1]
                else:
                    return v1_lst[i]
        else: return v1_lst[i]

        
class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

