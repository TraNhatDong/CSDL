class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None

    def RutGon(self):
        if self.Head is None or self.Head.KeTiep is None:
            return
        self.SapXep()
        current = self.Head
        while current and current.KeTiep:
            if current.SoMu == current.KeTiep.SoMu:
                current.HeSo += current.KeTiep.HeSo
                current.KeTiep = current.KeTiep.KeTiep
            else:
                current = current.KeTiep
        self.LoaiBoSoHangHeSoKhong()

    def SapXep(self):
        swapped = True
        while swapped:
            swapped = False
            current = self.Head
            while current.KeTiep:
                if current.SoMu < current.KeTiep.SoMu:

                    current.HeSo, current.KeTiep.HeSo = current.KeTiep.HeSo, current.HeSo
                    current.SoMu, current.KeTiep.SoMu = current.KeTiep.SoMu, current.SoMu
                    swapped = True
                current = current.KeTiep
    def Them(self, heso, somu):
        newNode = Node(heso, somu)
        if self.Head is None:
            self.Head = newNode
        else:
            current = self.Head
            while current.next:
                current = current.next
            current.next = newNode
    def LoaiBoSoHangHeSoKhong(self):
        dummy = Node(0, 0)
        dummy.KeTiep = self.Head
        prev = dummy
        current = self.Head
        while current:
            if current.HeSo == 0:
                prev.KeTiep = current.KeTiep
            else:
                prev = current
            current = current.KeTiep
        self.Head = dummy.KeTiep

dathuc = DaThuc()
dathuc.Them(2,3)
dathuc.Them(-4,6)
dathuc.RutGon()

