class TreeNode:
    def __init__(self, key):
        self.left = None
        self.right= None
        self.value= key

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

#прямий обхід
    def sum_pre_order(self):
       return self._sum_pre_order(self.root)
    
    def _sum_pre_order(self, node):
       if node is None:
          return 0 
       return node.value + self._sum_pre_order(node.left) + self._sum_pre_order(node.right)
    
bst = BinarySearchTree()

values = [8, 3, 10, 1, 6, 14, 4, 7, 13]
for val in values:
   bst.insert(val)

print("Сума значень при прямому обході:", bst.sum_pre_order())
