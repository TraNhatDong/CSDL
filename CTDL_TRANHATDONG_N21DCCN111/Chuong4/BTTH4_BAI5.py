class HanoiTower:
    def __init__(self, n):
        self.n = n

    def moveTower(self, n, source, destination, auxiliary):
        if n == 1:
            print(f"Chuyển tầng {n} từ cột {source} đến cột {destination}")
            return
        self.moveTower(n-1, source, auxiliary, destination)
        print(f"Chuyển tầng {n} từ cột {source} đến cột {destination}")
        self.moveTower(n-1, auxiliary, destination, source)

n = 3
hanoi = HanoiTower(n)
hanoi.moveTower(n, '1', '3', '2')
