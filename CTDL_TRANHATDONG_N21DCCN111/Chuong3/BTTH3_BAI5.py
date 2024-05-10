class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None
    def Tich(self, dathuc2):
        ketQua = DaThuc()
        current1 = self.Head
        while current1:
            current2 = dathuc2.Head
            while current2:
                newHeSo = current1.HeSo * current2.HeSo
                newSoMu = current1.SoMu + current2.SoMu
                ketQua.Them(newHeSo, newSoMu)
                current2 = current2.KeTiep
            current1 = current1.KeTiep


        ketQua.RutGon()

        return ketQua

dathuc1 = DaThuc()
dathuc2 = DaThuc()
dathucKetQua = dathuc1.Tich(dathuc2)
