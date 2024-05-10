class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None

def areIdentical(root1, root2):
    if root1 is None and root2 is None:
        return True
    if root1 is None or root2 is None:
        return False
    return (root1.info == root2.info) and areIdentical(root1.left, root2.left) and areIdentical(root1.right, root2.right)

def CayCon(root1, root2):
    if root2 is None:
        return True
    if root1 is None:
        return False
    if areIdentical(root1, root2):
        return True
    return CayCon(root1.left, root2) or CayCon(root1.right, root2)
cay1 = Node(1)
cay1.left = Node(2)
cay1.right = Node(3)
cay1.left.left = Node(4)
cay1.left.right = Node(5)

cay2 = Node(2)
cay2.left = Node(4)
cay2.right = Node(5)
print("cay2 là cây con của cay1:", CayCon(cay1, cay2))
