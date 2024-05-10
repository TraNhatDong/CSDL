class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def countNodes(root):
    if root is None:
        return 0
    return 1 + countNodes(root.left) + countNodes(root.right)


root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)


print("Số nút của cây là:", countNodes(root))
