class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def ChieuCao(node):
    if node is None:
        return 0
    else:
        chieuCaoTrai = ChieuCao(node.left)
        chieuCaoPhai = ChieuCao(node.right)
        return max(chieuCaoTrai, chieuCaoPhai) + 1

root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)

print("Chiều cao của cây là:", ChieuCao(root))
