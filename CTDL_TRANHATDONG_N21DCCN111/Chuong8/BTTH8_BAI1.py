class TuDien:
    def __init__(self):
        self.tu_dien = {}

    def NhapTu(self, tu, dong_nghia=None, trai_nghia=None):
        key = tu[0]
        if key not in self.tu_dien:
            self.tu_dien[key] = []
        self.tu_dien[key].append({'tu': tu, 'dong_nghia': dong_nghia, 'trai_nghia': trai_nghia})

    def TraTu(self, tu):
        key = tu[0]
        if key in self.tu_dien:
            for entry in self.tu_dien[key]:
                if entry['tu'] == tu:
                    return entry['dong_nghia'], entry['trai_nghia']
        return None, None
td = TuDien()
td.NhapTu('tốt', dong_nghia='tuyệt vời', trai_nghia='xấu')
td.NhapTu('vui', dong_nghia='hạnh phúc', trai_nghia='buồn')

print(td.TraTu('tốt'))
print(td.TraTu('vui'))
