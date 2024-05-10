class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def countNodes(node):
    if node is None:
        return 0
    return 1 + countNodes(node.left) + countNodes(node.right)
def CanBangHoanToan(node):
    if node is None:
        return True
    left_count = countNodes(node.left)
    right_count = countNodes(node.right)
    if abs(left_count - right_count) <= 1 and CanBangHoanToan(node.left) and CanBangHoanToan(node.right):
        return True
    else:
        return False
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Cây này cân bằng hoàn toàn:", CanBangHoanToan(root))
