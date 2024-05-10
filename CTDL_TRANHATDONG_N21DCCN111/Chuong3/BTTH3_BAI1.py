class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.next = None

class DaThuc:
    def __init__(self):
        self.Head = None
    def Them(self, heso, somu):
        newNode = Node(heso, somu)
        if self.Head is None:
            self.Head = newNode
        else:
            current = self.Head
            while current.next:
                current = current.next
            current.next = newNode

dathuc = DaThuc()
dathuc.Them(4, 3)
dathuc.Them(-2, 1)
