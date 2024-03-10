class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

def insert(root, key):
    if root is None:
        return TreeNode(key)
    if key < root.key:
        root.left = insert(root.left, key)
    else:
        root.right = insert(root.right, key)
    return root

def find_max(root):
    while root.right is not None:
        root = root.right
    return root.key

root = None
keys = [15, 10, 20, 8, 12, 17, 25]

for key in keys:
    root = insert(root, key)

max_value = find_max(root)
print("Найбільше значення в дереві:", max_value)