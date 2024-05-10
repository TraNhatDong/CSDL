class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

class BinaryTree:
    def __init__(self, root_info):
        self.root = Node(root_info)

    def SoSanh(self, node1, node2):
        if node1 is None and node2 is None:
            return True
        if node1 is None or node2 is None:
            return False
        return (node1.info == node2.info) and self.SoSanh(node1.left, node2.left) and self.SoSanh(node1.right, node2.right)
cay1 = BinaryTree(1)
cay1.root.left = Node(2)
cay1.root.right = Node(3)

cay2 = BinaryTree(1)
cay2.root.left = Node(2)
cay2.root.right = Node(3)
print("Hai cây giống hệt nhau:", cay1.SoSanh(cay1.root, cay2.root))
