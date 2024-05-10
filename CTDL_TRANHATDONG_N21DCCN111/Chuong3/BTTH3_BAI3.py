class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None
    def Cong(self, dathuc2):
        ketQua = DaThuc()
        current = self.Head
        while current:
            ketQua.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        current = dathuc2.Head
        while current:
            ketQua.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        ketQua.RutGon()
        return ketQua
dathuc1 = DaThuc()
dathuc2 = DaThuc()
dathucKetQua = dathuc1.Cong(dathuc2)
