class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.value = key

class BinarySearchTree:
    def __init__(self):
        self.root = None
        
    def insert(self, key):
        if self.root is None:
            self.root = TreeNode(key)
        else:
            self._insert(self.root, key)

    def _insert(self, node, key):
        if key < node.value:
            if node.left is None:
                node.left = TreeNode(key)
            else:
                self._insert(node.left, key) 
        else:
            if node.right is None:
                node.right = TreeNode(key)
            else:
                self._insert(node.right, key)

    def find_max(self):
        if self.root is None:
            return None
        return self._find_max(self.root)
    
    def _find_max(self, node):
        current = node
        while current.right is not None:
            current = current.right
        return current.value
# створення дерева
bst = BinarySearchTree()

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for val in values:
    bst.insert(val)

max_value = bst.find_max()
print("Найблыьше значення в дереві:", max_value)

