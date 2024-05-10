class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def SoNutLa(node):
    if node is None:
        return 0
    if node.left is None and node.right is None:
        return 1
    return SoNutLa(node.left) + SoNutLa(node.right)

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
print("Số nút lá của cây là:", SoNutLa(root))
