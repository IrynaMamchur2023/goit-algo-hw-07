class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

def find_min_bst(root):
    if root is None:
        return None
    
    current = root
    while current.left:
        current = current.left
    return current.val


root = TreeNode(8)
root.left = TreeNode(3)
root.right = TreeNode(10)
root.left.left = TreeNode(1)
root.left.right = TreeNode(6)
root.left.right.left = TreeNode(4)
root.left.right.right = TreeNode(7)
root.right.right = TreeNode(14)
root.right.right.left = TreeNode(13)

min_value = find_min_bst(root)
print("Найменше значення у дереві:", min_value)