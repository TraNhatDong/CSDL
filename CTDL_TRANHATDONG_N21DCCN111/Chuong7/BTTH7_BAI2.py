def SoThanhPhan(dt):
    visited = set()
    components = 0

    def dfs(v):
        if v not in visited:
            visited.add(v)
            for neighbor in dt[v]:
                dfs(neighbor)

    for vertex in dt:
        if vertex not in visited:
            dfs(vertex)
            components += 1

    return components
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C'],
    'E': ['F'],
    'F': ['E'],
    'G': []
}
print(SoThanhPhan(dt))
