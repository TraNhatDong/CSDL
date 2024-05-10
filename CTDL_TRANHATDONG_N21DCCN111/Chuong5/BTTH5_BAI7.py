class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
def Chep(node):
    if node is None:
        return None
    newNode = Node(node.info)
    newNode.left = Chep(node.left)
    newNode.right = Chep(node.right)

    return newNode
root = Node(1)
root.left = Node(2)
root.right = Node(3)
root.left.left = Node(4)
root.left.right = Node(5)
new_tree = Chep(root)
def printPreorder(node):
    if node:
        print(node.info, end=' ')
        printPreorder(node.left)
        printPreorder(node.right)


print("Cây gốc (preorder):", end=' ')
printPreorder(root)
print("\nCây sao chép (preorder):", end=' ')
printPreorder(new_tree)
