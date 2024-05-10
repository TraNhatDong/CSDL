class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def height(node):
    if node is None:
        return 0
    return max(height(node.left), height(node.right)) + 1
def KiemTraAVL(node):
    if node is None:
        return True
    left_height = height(node.left)
    right_height = height(node.right)
    if abs(left_height - right_height) > 1:
        return False
    return KiemTraAVL(node.left) and KiemTraAVL(node.right)
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Cây này là AVL:", KiemTraAVL(root))
