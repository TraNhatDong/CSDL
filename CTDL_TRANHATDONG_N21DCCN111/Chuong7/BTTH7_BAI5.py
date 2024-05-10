def BacDinh(dt, v):
    if v not in dt:
        return None
    return len(dt[v])
dt = {
    'A': ['B', 'C'],
    'B': ['A', 'D', 'E'],
    'C': ['A', 'F'],
    'D': ['B'],
    'E': ['B'],
    'F': ['C']
}
v = 'B'
print(BacDinh(dt, v))
