class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def SoNutTrungGian(node):
    if node is None or (node.left is None and node.right is None):
        return 0
    left_intermediate = SoNutTrungGian(node.left)
    right_intermediate = SoNutTrungGian(node.right)
    if (node.left is not None or node.right is not None) and node is not root:
        return left_intermediate + right_intermediate + 1
    else:
        return left_intermediate + right_intermediate
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Số nút trung gian của cây là:", SoNutTrungGian(root))
