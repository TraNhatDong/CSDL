class TuDien:
    def __init__(self):
        self.tu_dien = {}

    def NhapTu(self, tu, dong_nghia=[], trai_nghia=[]):
        key = tu[0].lower()
        if key not in self.tu_dien:
            self.tu_dien[key] = {}
        self.tu_dien[key][tu] = {'dong_nghia': dong_nghia, 'trai_nghia': trai_nghia}

    def DongNghia(self, tu):
        key = tu[0].lower()
        if key in self.tu_dien and tu in self.tu_dien[key]:
            return self.tu_dien[key][tu]['dong_nghia']
        return []

    def TraiNghia(self, tu):
        key = tu[0].lower()
        if key in self.tu_dien and tu in self.tu_dien[key]:
            return self.tu_dien[key][tu]['trai_nghia']
        return []
td = TuDien()
td.NhapTu('tốt', ['tuyệt vời', 'xuất sắc'], ['xấu', 'kém'])
td.NhapTu('vui', ['hạnh phúc', 'phấn khởi'], ['buồn', 'chán'])
print(td.DongNghia('tốt'))  # Kết quả sẽ là ['tuyệt vời', 'xuất sắc']
print(td.TraiNghia('vui'))  # Kết quả sẽ là ['buồn', 'chán']
