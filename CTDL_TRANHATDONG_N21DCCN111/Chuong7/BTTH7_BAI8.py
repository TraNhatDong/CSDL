def DuongDi(dt, v1, v2):
    visited = set()

    def dfs(v):
        if v == v2:
            return True
        visited.add(v)
        for neighbor in dt.get(v, []):
            if neighbor not in visited:
                if dfs(neighbor):
                    return True
        return False

    return dfs(v1)
dt = {
    'A': ['B', 'C'],
    'B': ['C', 'D'],
    'C': ['D'],
    'D': ['E'],
    'E': []
}
v1 = 'A'
v2 = 'E'
print(DuongDi(dt, v1, v2))
