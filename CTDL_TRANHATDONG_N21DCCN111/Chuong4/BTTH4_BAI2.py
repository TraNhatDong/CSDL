class Node:
    def __init__(self, info):
        self.info = info
        self.next = None
class DSLK:
    def __init__(self):
        self.head = None
    def themVaoDau(self, info):
        newNode = Node(info)
        newNode.next = self.head
        self.head = newNode
    def DaoNguoc(self):
        stack = []
        current = self.head
        while current is not None:
            stack.append(current)
            current = current.next
        self.head = stack.pop() if stack else None
        current = self.head
        while stack:
            current.next = stack.pop()
            current = current.next
        if current:
            current.next = None
    def inDSLK(self):
        current = self.head
        while current is not None:
            print(current.info, end=' ')
            current = current.next
        print()

dslk = DSLK()
dslk.themVaoDau(1)
dslk.themVaoDau(2)
dslk.themVaoDau(3)
dslk.themVaoDau(4)

print("DSLK ban đầu:")
dslk.inDSLK()
dslk.DaoNguoc()
print("DSLK sau khi đảo ngược:")
dslk.inDSLK()
