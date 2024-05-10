class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None
    def DoiDau(self):
        current = self.Head
        while current:
            current.HeSo = -current.HeSo
            current = current.KeTiep


dathuc = DaThuc()
dathuc.DoiDau()
