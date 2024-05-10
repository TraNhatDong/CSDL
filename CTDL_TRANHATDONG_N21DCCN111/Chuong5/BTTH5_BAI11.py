class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None


def BSTTuanTu(node):
    if node is None:
        return True
    if node.left is not None and node.right is not None:
        return False
    return BSTTuanTu(node.left) and BSTTuanTu(node.right)
root = Node(10)
root.left = Node(5)
root.left.left = Node(3)
root.left.left.left = Node(1)
print("Cây này là BST tuần tự:", BSTTuanTu(root))
