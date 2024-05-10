def LienThong(dt):
    visited = set()

    def dfs(v):
        if v not in visited:
            visited.add(v)
            for neighbor in dt[v]:
                dfs(neighbor)
    dfs(next(iter(dt)))
    return len(visited) == len(dt)
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C']
}
print(LienThong(dt))
