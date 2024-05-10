class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def KiemTraBST(node, left=None, right=None):
    if node is None:
        return True
    if (left is not None and node.info <= left.info) or (right is not None and node.info >= right.info):
        return False
    return KiemTraBST(node.left, left, node) and KiemTraBST(node.right, node, right)
root = Node(10)
root.left = Node(5)
root.right = Node(15)
root.left.left = Node(2)
root.left.right = Node(6)
root.right.left = Node(12)
root.right.right = Node(20)
print("Cây này là BST:", KiemTraBST(root))
