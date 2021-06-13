class TreeNode:
    def __init__(self, val, left, right):
        self.val = val
        self.left = left
        self.right = right
    def insert(self, root, val):
        if not root:
            return TreeNode(val)
        elif val > root.val: 
            root.right = self.insert(root.right, val)
        elif val < root.val:
            root.left = self.insert(root.left, val)
    def search(self, root, val):
        if not root:
            return None
        elif root.val == val:
            return root
        elif root.val > val:
            return self.search(root.left, val)
        else:
            return self.search(root.right, val)
    
class Heap:
    def __init__(self):
        self.root = None
    def insert(self, val):
        