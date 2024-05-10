class Album:
    def __init__(self, ten_album, danh_sach_bai_hat):
        self.ten_album = ten_album
        self.danh_sach_bai_hat = danh_sach_bai_hat

class BaiHat:
    def __init__(self, ten_bai_hat, nhac_si, ca_si):
        self.ten_bai_hat = ten_bai_hat
        self.nhac_si = nhac_si
        self.ca_si = ca_si

class TuDien:
    def __init__(self):
        self.albums = {}

    def NhapAlbum(self, album):
        # Sử dụng tên album làm khóa trong từ điển
        self.albums[album.ten_album] = album

    def XemAlbum(self, ten):
        if ten in self.albums:
            album = self.albums[ten]
            print(f"Tên Album: {album.ten_album}")
            for bai_hat in album.danh_sach_bai_hat:
                print(f"Bài hát: {bai_hat.ten_bai_hat}, Nhạc sĩ: {bai_hat.nhac_si}, Ca sĩ: {bai_hat.ca_si}")
        else:
            print("Album không tồn tại trong từ điển.")
bai_hat1 = BaiHat('Bài hát 1', 'Nhạc sĩ A', 'Ca sĩ X')
bai_hat2 = BaiHat('Bài hát 2', 'Nhạc sĩ B', 'Ca sĩ Y')
album = Album('Album 1', [bai_hat1, bai_hat2])

td = TuDien()
td.NhapAlbum(album)
td.XemAlbum('Album 1')
