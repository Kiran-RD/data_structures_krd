def height(root):
    if root is None: return 0
    elif root.left is None and root.right is None: return 0
    else: return max(height(root.left), height(root.right))+1
