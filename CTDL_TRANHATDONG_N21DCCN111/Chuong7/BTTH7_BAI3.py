def ChuTrinh(dt):
    visited = set()
    recStack = set()

    def dfs(v, parent):
        visited.add(v)
        recStack.add(v)
        for neighbor in dt[v]:
            if neighbor not in visited:
                if dfs(neighbor, v):
                    return True
            elif neighbor in recStack and neighbor != parent:
                return True
        recStack.remove(v)
        return False

    for vertex in dt:
        if vertex not in visited:
            if dfs(vertex, None):
                return True
    return False
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'D'],
    'C': ['A', 'D'],
    'D': ['B', 'C', 'E'],
    'E': ['D']
}
print(ChuTrinh(dt))
