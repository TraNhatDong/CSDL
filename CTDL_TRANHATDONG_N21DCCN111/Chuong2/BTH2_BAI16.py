def Dao(mang):
    n = len(mang)
    visited = [[False for _ in range(n)] for _ in range(n)]

    def is_rectangle(x1, y1, x2, y2):
        for i in range(x1, x2 + 1):
            for j in range(y1, y2 + 1):
                if mang[i][j] == 0:
                    return False
        return True

    def dfs(x, y):
        if x < 0 or x >= n or y < 0 or y >= n or mang[x][y] == 0 or visited[x][y]:
            return 0
        visited[x][y] = True
        area = 1
        area += dfs(x + 1, y)
        area += dfs(x - 1, y)
        area += dfs(x, y + 1)
        area += dfs(x, y - 1)
        return area

    max_area = 0
    for i in range(n):
        for j in range(n):
            if mang[i][j] == 1 and not visited[i][j]:
                x1, y1, x2, y2 = i, j, i, j
                while x2 + 1 < n and mang[x2 + 1][j] == 1:
                    x2 += 1
                while y2 + 1 < n and mang[i][y2 + 1] == 1:
                    y2 += 1
                if is_rectangle(x1, y1, x2, y2):
                    max_area = max(max_area, dfs(i, j))
    print(f"Diện tích lớn nhất của các đảo hình chữ nhật là: {max_area}")
mang = [
    [1, 1, 0, 0, 0],
    [1, 1, 0, 1, 1],
    [0, 0, 0, 1, 1],
    [0, 1, 1, 1, 0],
    [1, 1, 0, 0, 0]
]
Dao(mang)
