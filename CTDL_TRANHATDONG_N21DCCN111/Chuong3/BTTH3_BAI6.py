class Node:
    def __init__(self, heso, somu):
        self.HeSo = heso
        self.SoMu = somu
        self.KeTiep = None
class DaThuc:
    def __init__(self):
        self.Head = None
    def Chep(self):
        banSao = DaThuc()
        current = self.Head
        while current:
            banSao.Them(current.HeSo, current.SoMu)
            current = current.KeTiep
        return banSao
dathuc = DaThuc()
dathucBanSao = dathuc.Chep()
